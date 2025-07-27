import flet as ft


def main(page: ft.Page):
    page.title= "Custom Menu Component"
    page.padding=0
    page.spacing=0
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    page.bgcolor= "#EDEDE9"

    class Menuoption(ft.IconButton):
        def __init__(self, lcon):
            super().__init__(
                icon_size=36,
                icon=lcon,
                on_click=self.click,
            )
            self.icon_color = ft.Colors.BLACK
            self.bgcolor = ft.Colors.TRANSPARENT


        def click(self, e):
            self.icon_color= ft.Colors.WHITE
            self.bgcolor = ft.Colors.BLACK
            self.update()

    option1 = Menuoption(lcon=ft.Icons.HOME)


    page.add(
        ft.Container(
            bgcolor="#D5BDAF",
            width=80,
            height=120,
            border_radius=24,
            content=option1

        )
    )

ft.app(target=main)