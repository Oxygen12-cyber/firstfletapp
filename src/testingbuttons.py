import flet as ft


def main(page: ft.Page):
    name = ft.Text(value="")

    def show_name(e):
        name.value = "I am Oxygen"
        if not name.visible:
            name.visible = True
            page.update()
        page.update()

    def clear_data(e):
        if name.visible:
            name.visible = False
            page.update()

    page.add(
        name,
        ft.Button(text="click here", on_click=show_name),
        ft.IconButton(icon=ft.Icons.CLEAR, on_click=clear_data),
        ft.ElevatedButton(text="Login",)
    )

ft.app(main)