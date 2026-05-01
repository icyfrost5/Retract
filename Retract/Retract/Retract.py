import asyncio
import reflex as rx


class State(rx.State):
    pass

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
                sidebar_link("Image Generator", "image_plus", "/images", '4', "100%"),
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
def images():
    return rx.hstack(
        sidebar(),
        rx.box(
            rx.button(icon="settings", position="top-right",),
            bg=rx.color_mode_cond(light="#cceffa", dark="#111111"),
            width="100%",
            height="100vh"
        )
    )



app = rx.App()
app.add_page(index, "/")
app.add_page(images, "/images")
