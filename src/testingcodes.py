import flet as ft

def main(page: ft.Page):
    page.bgcolor="#1e1e1e"
    page.padding= 0
    page.spacing=0
    page.title="TestingCodes"
    page.horizontal_alignment="center"
    page.vertical_alignment="center"


    class MenuButton(ft.Button):
        def __init__(self):
            super().__init__()
            pass


    main_block = ft.Container(
        bgcolor=ft.Colors.BLACK,
        width=150,
        height=300,
        border_radius=24,
        alignment=ft.alignment.center,
        margin=ft.margin.only(top=140, bottom=50),
        content=ft.Container(
            padding=10,
            bgcolor=ft.Colors.BLACK,
            border=ft.border.all(1, ft.Colors.WHITE54),
            alignment=ft.alignment.center

        )

    )

    page.add(
        ft.Container(
            main_block,
            expand=True,
            bgcolor=ft.Colors.GREY_300,
        )
    )

ft.app(target=main)
