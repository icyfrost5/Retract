import asyncio

import reflex as rx


class State(rx.State):
    Loading = True
    colormodeicon = "moon_star"

    async def skeleton_wait_time(self):
        self.Loading = True
        await asyncio.sleep(0.2)
        self.Loading = False


@rx.page(on_load=State.skeleton_wait_time)
def index():
    # Welcome Page (Index)
    return rx.container(
        rx.skeleton(rx.color_mode.button(position="top-right"), loading=State.Loading),
        sidebar()
    )


def sidebar_link(text, icon, url, ):
    return rx.link(rx.hstack(rx.icon(icon, color=rx.color_mode_cond(light="rgb(0, 0, 0)", dark="rgb(255, 255, 255)")),
                             rx.text(text, size="5",
                                     color=rx.color_mode_cond(light="rgb(0, 0, 0)", dark="rgb(255, 255, 255)")),
                             align="center", width="100%", style={
            "_hover": {"bg": rx.color_mode_cond(light="rgb(220, 220, 220)", dark="rgb(50, 50, 50)")}}), href=url)


def sidebar():
    return rx.box(
        rx.vstack(
            sidebar_link("Home", "layout-dashboard", "/"),
            width="20%",
            spacing="5",
            bg=rx.color_mode_cond(light="rgb(240, 240, 240)", dark="rgb(27, 27, 27)"),
            align="start",

        ),

    )


app = rx.App()
app.add_page(index)
