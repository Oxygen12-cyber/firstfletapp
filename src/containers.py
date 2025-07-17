import flet as ft

def main(page: ft.Page):
    page.title="Testing containers"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.theme_mode=ft.ThemeMode.SYSTEM

    page.add(
        ft.Row([
            ft.Container(
                content=ft.Text("A container",color=ft.Colors.WHITE),
                bgcolor=ft.Colors.AMBER_200,
                alignment=ft.alignment.center,
                width=100,
                height=100,
                border_radius=12
            ),
            ft.Container(
                content=ft.Text("A container"),
                bgcolor=ft.Colors.BLUE_200,
                alignment=ft.alignment.center,
                width=100,
                height=100,
                margin=60,
                on_click=lambda e: print("Clickable without Ink clicked!")
            ),
            ft.Container(
                content=ft.Text("A container"),
                bgcolor=ft.Colors.BLUE_GREY_200,
                alignment=ft.alignment.center,
                width=100,
                height=100
            )


        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(main)