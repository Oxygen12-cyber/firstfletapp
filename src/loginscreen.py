import flet as ft


def main(page: ft.Page):
    # page.vertical_alignment = ft.MainAxisAlignment.START
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {
        "inter-smbold": "fonts/Inter_24pt-Bold.ttf",
        "inter-sm": "fonts/Inter_24pt-Medium.ttf",
        "inter-bm": "fonts/Inter_28pt-Medium.ttf",
        "inter-italic": "fonts/Inter_24pt-Italic.ttf",
    }
    page.theme = ft.Theme(font_family="inter-italic")

    def show_password(e):
        login_field.password = False
        login_field.update()

    background = ft.Container(
            content=ft.Image(
                src="images/origbg.jpg",
                fit=ft.ImageFit.COVER,
                expand=True,
            ),
        expand=True,
        alignment=ft.alignment.center
    )
    login_field = ft.TextField(
        label="Your Password",
        password=True,
        min_lines=12,
        border_radius=36,
        border_color=ft.Colors.WHITE,
        suffix_icon=ft.IconButton(ft.Icons.VISIBILITY, on_click=show_password)
    )
    profile_image = ft.Container(
        content=ft.Image(
            src="images/icon.png",
            fit=ft.ImageFit.COVER,
        ),
        border_radius=600,
        padding=2,
        bgcolor=ft.Colors.BLUE_50,
        border=ft.border.all(2, ft.Colors.BLACK26),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        animate=ft.Animation(duration=300, curve=ft.AnimationCurve.EASE_IN_OUT)
    )

    page.add(
        ft.Stack(
            [
                background,

                ft.Container(
                    content=
                        ft.Column(
                            [
                                ft.Container(
                                    content=ft.Container(
                                        content=profile_image,
                                        width=200,
                                        height=200,
                                    ),
                                    expand=True,
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        value="Oxygen",
                                        size=40,
                                        style=ft.TextStyle(),
                                        font_family="inter-bm",
                                        color=ft.Colors.WHITE,
                                    ),
                                    expand=True,
                                    margin=ft.margin.only(top=30),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Container(content=login_field, width=300, expand=False),
                                            ft.Container(
                                                ft.ProgressRing(
                                                    width=24,
                                                    height=24,
                                                    stroke_width=4,
                                                    color=ft.Colors.BLACK,
                                                    visible=False
                                                ),
                                                margin=ft.margin.only(left=20)
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),

                                    expand=True,
                                    margin=ft.margin.only(top=20),
                                    alignment=ft.alignment.center
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),

                )
            ]
        )
    )


ft.app(main, assets_dir="src/assets")
