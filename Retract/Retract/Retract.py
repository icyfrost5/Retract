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
    return rx.hstack(
        sidebar(),
        rx.box(
            rx.skeleton(rx.color_mode.button(position="top-right"), loading=State.Loading),
            margin_left="200px"
        )
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
            rx.vstack(
                sidebar_link("Home", "layout-dashboard", "/"),
                spacing="5",
                align="start"
            ),
            spacing="5",
            bg=rx.color_mode_cond(light="rgb(240, 240, 240)", dark="rgb(27, 27, 27)"),
            align="start",
            position="fixed",
            padding_y=".75em",
            padding_x="1em",
            justify = "start",
            flex_wrap = "wrap",
            width="200px"
        )
    )


app = rx.App()
app.add_page(index)
