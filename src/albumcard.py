import flet as ft


def main(page: ft.Page):
    page.title = 'card example'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.ALBUM),
                            title=ft.Text("the Enchanted"),
                            subtitle=ft.Text("music by Julie gable. Lyrics by sidney Stein"),
                            bgcolor=ft.Colors.GREY_400,
                            ),
                        ft.Row(
                            [ft.TextButton("Buy Tickets"), ft.TextButton("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),    
                    ]
                ),
                width=400,
                padding=10
            ),
            shadow_color=ft.Colors.PINK,
        ),
        
    )



ft.app(main)