import flet as ft


def main(page: ft.Page):
    count = ft.Text(value="0", size=30)

    def increment(e):
        count.value = str(int(count.value) + 1)
        page.update()

    def decrement(e):
        if count.data == 0:
            ft.Text("number is already zero")
            page.update()
        else:
            count.value = str(int(count.value) - 1)
            page.update()

    page.add(
        ft.Row([
        count,
        ft.FloatingActionButton(icon=ft.Icons.REMOVE, on_click=decrement),
        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=increment) 
        ])
    )

ft.app(main)