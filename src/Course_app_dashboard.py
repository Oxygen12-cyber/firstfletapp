import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#ffffff"
    page.title = "Course App Dashboard"
    page.padding = 0
    page.spacing = 0
    page.margin = 0
    page.scroll = "adaptive"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.border = 0
    page.fonts = {"jua": "fonts/Jua-Regular.ttf"}
    page.theme = ft.Theme(font_family="jua")

    page.theme_mode = ft.ThemeMode.LIGHT

    class UIcard(ft.Card):
        def __init__(self, c_width, c_height):
            super().__init__(
                color="#f5f5f7",
                width=c_width,
                height=c_height,
                elevation=2,
            )

    class UIbutton(ft.ElevatedButton):
        def __init__(self, text):
            super().__init__(
                bgcolor="#000000",
                color="#FEFEFE",
                text=text,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),padding=ft.padding.only(left=14,right=14,top=18,bottom=18)),
                elevation=2,
            )

    class UIlistitem(ft.Container):
        def __init__(self, imagesrc, titletext, subtext, time, users):
            super().__init__(
                bgcolor="#f5f5f7",
                border_radius=12,
            )
            self.image = ft.Image(src=imagesrc, width=64, height=64, fit=ft.ImageFit.COVER)
            self.titletext = ft.Text(value=titletext, size=20, color="#000000", weight=ft.FontWeight.BOLD)
            self.subtext = ft.Text(value=subtext, size=12, color="#070707", weight=ft.FontWeight.NORMAL)
            self.time = ft.Text(value=time, size=14, color="#070707", weight=ft.FontWeight.NORMAL)
            self.users = ft.Text(value=users, size=14, color="#070707", weight=ft.FontWeight.NORMAL)
            time_icon = ft.Icon(name="access_time_filled", color="#070707")
            user_icon = ft.Icon(name="whatshot", color="#070707")
            self.content = ft.Row(
                controls=[
                    ft.Container(
                        ft.Row(
                            controls=[
                                ft.Container(self.image, margin=ft.margin.only(left=4, top=4, bottom=4, right=6),
                                             bgcolor="white", border_radius=8),
                                ft.Column(
                                    [self.titletext, self.subtext],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
                                    tight=True,
                                    spacing=0
                                ),
                                ft.Container(ft.Row([time_icon, self.time], tight=True, spacing=2)),
                                ft.Container(ft.Row([user_icon, self.users], tight=True, spacing=2),
                                             padding=ft.padding.only(right=0)),
                                UIbutton(text="View Course")
                            ],
                            spacing=15
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )

    class Menuitem(ft.Container):
        def __init__(self, icon, tooltip_text):
            super().__init__(
                bgcolor="transparent",
                tooltip=tooltip_text,
                ink=False,
                on_click=self.on_click,
                content = ft.Icon(name=icon, color="")
            )
        def on_click(self, e):
            pass

    ui = UIlistitem(
        imagesrc="images/icon.png",
        titletext="Flet Course",
        subtext="Learn Flet with this course",
        time="2 hours ago",
        users="5 users"
    )
    menu = Menuitem(
        icon=ft.Icons.HOME,
        tooltip_text="home"
    )

    page.add(
        ft.Container(
            ft.Column(
                controls=[
                    ui,
                    menu
                ]
            ),
            margin=ft.margin.only(top=80,left=100, right=80),
        )
    )


ft.app(target=main, assets_dir="src/assets")
