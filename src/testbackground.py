import flet as ft



def main(page: ft.Page):
    page.padding=0
    page.spacing=0
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    page.title="Test Background"


    background = ft.Container(
        ft.Image(
            src="images/origbg.jpg",
            fit=ft.ImageFit.COVER,
        )
    )
    center_block = ft.Container(
        alignment=ft.alignment.center,
        border_radius=12,
        width=350,
        height=350,
        bgcolor="black",
        margin=ft.margin.only(top=140),
    )
    # login = ft.Card(color="white", width=200, height=300, margin=ft.margin.only(top=20, bottom=80),)
    page.add(
        ft.Stack([
            # ft.Container(content=background,expand=True),
            background,
            ft.Row([center_block], alignment=ft.MainAxisAlignment.CENTER),

        ])
    )




ft.app(main, assets_dir="src/assets")