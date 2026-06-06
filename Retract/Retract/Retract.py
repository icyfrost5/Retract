import asyncio

import reflex as rx
import subprocess
import os



def installcommand():
    subprocess.run(["python", "-m", "pip", "install", "yt-dlp"], check=True, capture_output=True, text=True)


class DownloaderState(rx.State):
    nohasytdlppath = False
    failpathdownload = False
    Disable = False
    text = "Install using python"
    Link = "Failed to download using pip, please ", rx.link("download", href="https://github.com/yt-dlp/yt-dlp/releases/download/2026.03.17/yt-dlp.exe") , " it and put it in the assets directory"

    async def check_for_ytdlp_path(self):
        try:
            os.chdir('assets')
            subprocess.run(["yt-dlp", "--update"], check=True, capture_output=True, text=True)
            os.chdir('..')
            self.nohasytdlppath = False
        except (FileNotFoundError, subprocess.CalledProcessError):
            os.chdir('..')
            self.nohasytdlppath = True
    async def install_ytdlp_python(self):
        try:
            self.Disable = True
            self.text = "Installing..."
            yield
            await asyncio.to_thread(installcommand)
            self.nohasytdlppath = False
            self.Disable = False
            self.text = "Success!"
            yield rx.toast.success("Successfully installed yt-dlp using python")
        except (FileNotFoundError, subprocess.CalledProcessError, ModuleNotFoundError):
            self.failpathdownload = True
            self.text = "Failed to install"
            self.Disable = False
            yield rx.toast.error(self.Link)
        self.text = "Install using python"


def sidebar_link(text, icon, url, size, width):
    return rx.link(rx.hstack(rx.icon(icon, color=rx.color_mode_cond(light="#0A0F1E", dark="#C8A96E")),
                             rx.text(text, size=size,
                             color=rx.color_mode_cond(light="#0A0F1E", dark="#C8A96E")),
                             align="center", width=width, style={
                                "_hover": {"bg": rx.color_mode_cond(light="#d8f2fa", dark="#282828")}}), href=url)

def sidebar():
    return rx.box(
        rx.vstack(
            rx.vstack(
                sidebar_link("Home", "layout-dashboard", "/", '5', "130%"),
                sidebar_link("Downloader", "download", "/downloader", '3', "100%"),
                spacing="5",
                align="start"
            ),
            spacing="5",
            bg=rx.color_mode_cond(light="#bfe9f7", dark="#1e1e1e"),
            align="start",
            position="fixed",
            padding_y=".75em",
            padding_x="1em",
            justify = "start",
            flex_wrap = "wrap",
            width="150px",
            height="100vh"
        )
    )

def index():
    # Welcome Page (Index)
    return rx.hstack(
        sidebar(),
        rx.box(
            rx.color_mode.button(position="top-right",color=rx.color_mode_cond(light="#0A0F1E", dark="#C8A96E")),
            bg=rx.color_mode_cond(light="#cceffa", dark="#111111"),
            width="100%",
            height="100vh"
        ),
    )

@rx.page(on_load=DownloaderState.check_for_ytdlp_path)
def downloader():
    return rx.hstack(
        sidebar(),
        rx.box(
            rx.dialog.root(
                rx.dialog.content(
                    rx.dialog.title("Warning"),
                    rx.dialog.description(""),
                    rx.dialog("yt-dlp is not detected and is required for this to work! Please either return to home, ", rx.link("download", href="https://github.com/yt-dlp/yt-dlp/releases/download/2026.03.17/yt-dlp.exe") ," it and put it in the assets directory, or install it using python if your python packages are in PATH."),
                    rx.dialog.close(rx.button("Return to home", on_click=rx.redirect("/")), rx.spacer(), rx.button(DownloaderState.text, rx.spinner(loading=DownloaderState.Disable), on_click=DownloaderState.install_ytdlp_python)),
                ),
                open=DownloaderState.nohasytdlppath,
            ),
            bg=rx.color_mode_cond(light="#cceffa", dark="#111111"),
            padding_left="135px",
            width="100%",
            height="100vh",
        )
    )



app = rx.App()
app.add_page(index, "/")
app.add_page(downloader, "/downloader")
