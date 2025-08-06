import flet as ft
from Course_app_dashboard import UIbutton
from Course_app_dashboard import UIlistitem





def main(page: ft.Page):
    page.bgcolor = "#1e1e1e"
    page.padding = 30

    tab = ft.Tabs(
        selected_index=0,
        label_color="black",
        label_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        indicator_color="black",
        animation_duration=1000,
        indicator_thickness=4,
        overlay_color="transparent",
        divider_color="transparent",
        tab_alignment=ft.TabAlignment.START_OFFSET,
        unselected_label_color=ft.Colors.GREY_600,
        tabs=[
            ft.Tab(
                text="All Courses",
                content=ft.ListView(
                    [
                        UIlistitem("Friends", "this is good", time="now", users="5", button_text="clickme")
                    ],
                    spacing=10,
                    padding=20
                )
            ),
            ft.Tab(text="The Newest"),
            ft.Tab(text="Top Rated"),
            ft.Tab(text="Most Popular"),
        ]
    )

    tabmode = ft.Container(
        ft.Column(
            [tab],
            scroll=ft.ScrollMode.AUTO,
            # horizontal_alignment=ft.CrossAxisAlignment.START
        ),
        width=1200,
        height=400,
        bgcolor="grey",

    )


page.add(tabmode)
ft.app(target=main)
