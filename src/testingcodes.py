import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#888581"
    page.padding = 0
    page.spacing = 0
    page.title = "TestingCodes"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    menu_button = ft.IconButton(icon=ft.Icons.LOCK_CLOCK_SHARP, icon_color="white")

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        bgcolor="#2f2f2d",
                        height=400,
                        width=100,
                        border_radius=24,
                        shadow=ft.BoxShadow(
                            blur_radius=15,
                            spread_radius=1,
                            offset=ft.Offset(0, 0),
                            color="2f2f2d",
                            blur_style=ft.ShadowBlurStyle.SOLID,
                        ),
                        padding=ft.padding.all(12),
                        content=ft.Container(
                            bgcolor="#2f2f2d",
                            height=400,
                            width=100,
                            border_radius=12,
                            border=ft.border.all(1, color="#ffffff"),
                            alignment=ft.alignment.center,
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        bgcolor="#2f2f2d",
                                        height=60,
                                        width=60,
                                        border_radius=12,
                                        padding=ft.padding.all(5),
                                        shadow=ft.BoxShadow(
                                            blur_radius=12,
                                            spread_radius=1,
                                            offset=ft.Offset(0, 0),
                                            # blur_style="solid"

                                        ),
                                        content=menu_button,
                                        margin=ft.margin.only(top=5)
                                    )
                                ],
                            )
                        )
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
    )


ft.app(main)
