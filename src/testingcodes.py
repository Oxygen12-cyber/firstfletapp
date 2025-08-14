import flet as ft
from Course_app_dashboard import UIcardcontainer
from Course_app_dashboard import UIlistitem


def main(page: ft.Page):
    page.bgcolor = "#1e1e1e"
    page.padding = 30
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER

    center_card = UIcardcontainer(
        500,
        150,
    )
    card_image = ft.Container(
        ft.Image(
            src="images/actor.png",
            fit=ft.ImageFit.CONTAIN
        ),
        width=256,
        height=256,
        # bgcolor="grey"
    )

    stack_layout = ft.Stack(
        [center_card, card_image],
        alignment=ft.alignment.bottom_right
    )

    #building component illegally here
    search_comp = ft.Container(
        ft.Row(
            [
                ft.Container(
                   ft.TextField(
                       prefix_icon=ft.Icon(name=ft.Icons.SEARCH_OUTLINED, color="black"),
                       hint_text="Search Courses",
                       hint_style=ft.TextStyle(color=ft.Colors.GREY_700),
                       border_color="transparent",
                       bgcolor="#f5f5f7",
                       focused_bgcolor="#f5f5f7",
                       focused_border_width=1,
                       focused_border_color="black",
                       border_radius=12,
                       cursor_color="black",

                       max_length=30,

                   )
                ),
                ft.Container(
                    ft.Row(
                        [
                            ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color="black"),
                            ft.IconButton(icon=ft.Icons.ARROW_FORWARD_ROUNDED, icon_color="black"),
                            ft.IconButton(icon=ft.Icons.ARROW_DROP_DOWN_OUTLINED, icon_color="black")
                        ],
                    )
                )
            ]
        ),
        expand=True
    )



    page.add(search_comp)
ft.app(target=main)



