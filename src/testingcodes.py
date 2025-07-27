import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#888581"
    page.padding = 0
    page.spacing = 0
    page.title = "TestingCodes"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    menu_button = ft.IconButton(
        icon=ft.Icons.LOCK_CLOCK_SHARP,
        width=64, height=64, bgcolor="black",
        icon_color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    class CustomMenubar(ft.Container):
        def __init__(self, expand_const: int):
            super().__init__(
                height=400,
                bgcolor="#2f2f2d",
                border_radius=24,
                shadow=ft.BoxShadow(
                    blur_radius=15,
                    spread_radius=1,
                    offset=ft.Offset(0, 0),
                    color="2f2f2d",
                    blur_style=ft.ShadowBlurStyle.SOLID,
                ),
                padding=ft.padding.all(12),
                content=ft.Column([menu_button], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ink=False,
                on_hover=self.onhover,
                animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT)
            )
            self.width = 100
            self.expand_const = expand_const
            self.current_state = 0

        def onhover(self, e):
            if e.data:
                self.current_state = 1
                self.width = self.expand_const
                self.update()
            elif not e.data and self.current_state == 1:
                self.width = self.expand_const
                self.current_state = 0
            self.update()

    menu_button = ft.IconButton(icon=ft.Icons.LOCK_CLOCK_SHARP, icon_color="white")
    menu = CustomMenubar(expand_const=400)

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[menu],
                alignment=ft.MainAxisAlignment.START,
            ),
            margin=ft.margin.only(left=100)
        )
    )


ft.app(main)
