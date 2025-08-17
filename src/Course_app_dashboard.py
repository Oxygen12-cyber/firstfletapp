import flet as ft


class UIcardcontainer(ft.Container):
    def __init__(self, c_width=None, c_height=None, content=None, padding=None, expansion=False):
        super().__init__(
            bgcolor="#f5f5f7",
            width=c_width,
            height=c_height,
            border_radius=12
        )
        self.content = content
        self.expand=expansion
        self.padding=padding


class UIbutton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__(
            bgcolor="#000000",
            color="#FEFEFE",
            text=text,
            on_click=self.on_click,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),
                                 padding=ft.padding.only(left=14, right=14, top=18, bottom=18)),
            elevation=2,
        )

    def on_click(self, e):
        pass

class UIlistitem(ft.Container):
    def __init__(self, titletext, subtext, time=None, users=None, imagesrc="images/icon.png", button_text=None, expansion=False):
        super().__init__(
            bgcolor="#f5f5f7",
            border_radius=12,
        )
        self.image = ft.Image(src=imagesrc, width=48, height=48, fit=ft.ImageFit.COVER)
        self.expand=expansion
        self.titletext = ft.Text(value=titletext, size=20, color="#000000", weight=ft.FontWeight.BOLD)
        self.subtext = ft.Text(value=subtext, size=12, color="#070707", weight=ft.FontWeight.NORMAL)
        self.time = ft.Text(value=time, size=14, color="#070707", weight=ft.FontWeight.NORMAL)
        self.users = ft.Text(value=users, size=14, color="#070707", weight=ft.FontWeight.NORMAL)
        time_icon = ft.Icon(name="access_time_filled", color="#070707")
        user_icon = ft.Icon(name="whatshot", color="#070707")
        self.button_text = button_text
        self.content = ft.Row(
            controls=[
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                self.image,
                                margin=ft.margin.only(left=4, top=4, bottom=4, right=6),
                                bgcolor="white", border_radius=8
                            ),
                            ft.Container(
                                ft.Column(
                                    [self.titletext, self.subtext],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
                                    spacing=0
                                ),
                            ),
                            ft.Container(ft.Row([time_icon, self.time],expand=True, spacing=2)),
                            ft.Container(ft.Row([user_icon, self.users], expand=True,spacing=2),
                                         padding=ft.padding.only(right=0)),
                            UIbutton(text=self.button_text),
                        ],
                        spacing=15,
                        tight=True
                    ),
                    margin=ft.margin.all(10)
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )


class Menuitem(ft.Container):
    def __init__(self, icon, tooltip_text):
        super().__init__(
            bgcolor="transparent",
            tooltip=tooltip_text,
            on_click=self.on_click,
            ink=False,
            content=ft.Icon(name=icon, color=ft.Colors.GREY_500)
        )

    def on_click(self, e):
        pass


def main(page: ft.Page):
    page.bgcolor = "#ffffff"
    page.title = "Course App Dashboard"
    page.padding = 0
    page.spacing = 0
    page.margin = 0
    # page.scroll = "adaptive"
    # page.scrollable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.border = 0
    page.fonts = {"jua": "fonts/Jua-Regular.ttf","inter": "fonts/Inter_24pt-Medium.ttf"}
    page.theme = ft.Theme(font_family="inter")
    page.theme_mode = ft.ThemeMode.LIGHT

    # definition of menu icons
    mhome = Menuitem(icon=ft.Icons.HOME_OUTLINED, tooltip_text="Home")
    medu = Menuitem(icon=ft.Icons.SCHOOL_OUTLINED, tooltip_text="Courses")
    mprofile = Menuitem(icon=ft.Icons.PERSON, tooltip_text="profile")
    mmail = Menuitem(icon=ft.Icons.MAIL_OUTLINED, tooltip_text="Messages")
    msettings = Menuitem(icon=ft.Icons.SETTINGS, tooltip_text="Settings")
    mlogout = Menuitem(icon=ft.Icons.LOGOUT, tooltip_text="Logout")

    # tab drop definition
    tabmode = ft.Container(
        ft.Tabs(
            selected_index=0,
            label_color="black",
            label_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
            indicator_color="black",
            animation_duration=1000,
            indicator_thickness=4,
            overlay_color="transparent",
            divider_color="transparent",
            tab_alignment=ft.TabAlignment.START,
            unselected_label_color=ft.Colors.GREY_600,
            tabs=[
                ft.Tab(
                    text="All Courses",
                    content=ft.Container(
                        ft.ListView(
                            [
                                UIlistitem("Friends", "this is good", time="now", users="5",
                                           button_text="clickme") for _ in range(20)
                            ],
                            spacing=10,
                            padding=ft.padding.only(top=20,bottom=30)
                        ),
                        width=600,
                        height=200
                    )
                ),
                ft.Tab(text="The Newest"),
                ft.Tab(text="Top Rated"),
                ft.Tab(text="Most Popular")
            ]
        ),
        alignment=ft.alignment.center_left,
        width=600,
        height=400,
    )

    # menubar definition
    menubar = ft.Container(
        padding=24,
        alignment=ft.alignment.center,
        bgcolor="#000000",
        ink=False,
        border_radius=20,
        margin=ft.margin.only(top=40, bottom=40, left=20, ),
        shadow=ft.BoxShadow(
            blur_radius=15,
            spread_radius=3,
            offset=ft.Offset(0, 0),
            color=ft.Colors.BLACK12,
            blur_style=ft.ShadowBlurStyle.SOLID,
        ),
        content=ft.Column(
            [
                ft.Container(
                    ft.Image(src="images/oxygenlogo-white.png", fit=ft.ImageFit.COVER),
                    width=55,
                    height=55
                ),
                ft.Container(
                    ft.Column(
                        [mhome, medu, mprofile, mmail, msettings],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        spacing=30,
                    ),
                    margin=ft.margin.only(top=40)
                ),
                ft.Container(mlogout, margin=ft.margin.only(top=230)),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    )

    #hello image popup
    hi_image = ft.Container(
        ft.Image(
            src="images/vecteezy-actor.png",
            fit=ft.ImageFit.COVER
        ),
        width=200,
        height=200,
        # bgcolor="grey",
        margin=ft.margin.only(right=30)

    )

    #chart
    chart = ft.Container(
        ft.LineChart(
            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(value=0, label=ft.Text("0", font_family="jua", color="black", size=14)),
                    ft.ChartAxisLabel(value=1, label=ft.Text("1", font_family="jua", color="black", size=14)),
                    ft.ChartAxisLabel(value=2, label=ft.Text("2", font_family="jua", color="black", size=14)),
                    ft.ChartAxisLabel(value=3, label=ft.Text("3", font_family="jua", color="black", size=14)),
                    ft.ChartAxisLabel(value=4, label=ft.Text("4", font_family="jua", color="black", size=14)),
                    ft.ChartAxisLabel(value=5, label=ft.Text("5", font_family="jua", color="black", size=14)),
                ]
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(value=0, label=ft.Text("mon", font_family="jua", color="black", size=14,
                                                             weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=1, label=ft.Text("tue", font_family="jua", color="black", size=14,
                                                             weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=2, label=ft.Text("wed", font_family="jua", color="black", size=14,
                                                             weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=3, label=ft.Text("thu", font_family="jua", color="black", size=14,
                                                             weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=4, label=ft.Text("fri", font_family="jua", color="black", size=14,
                                                             weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=5, label=ft.Text("sat", font_family="jua", color="black", size=14,
                                                             weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=6, label=ft.Text("sun", font_family="jua", color="black", size=14,
                                                             weight=ft.FontWeight.BOLD)),
                ]
            ),
            data_series=[
                ft.LineChartData(
                    [
                        ft.LineChartDataPoint(0, 0),
                        ft.LineChartDataPoint(1, 1.5),
                        ft.LineChartDataPoint(2, 2.5),
                        ft.LineChartDataPoint(3, 1),
                        ft.LineChartDataPoint(4, 4),
                        ft.LineChartDataPoint(5, 3),
                        ft.LineChartDataPoint(6, 2)
                    ],
                    stroke_width=3,
                    color=ft.Colors.BLACK,
                    stroke_cap_round=True,
                    curved=True,
                    point=ft.ChartCirclePoint(color="black", stroke_width=2),

                )
            ],
            point_line_start=0,
            point_line_end=0,
            tooltip_bgcolor=ft.Colors.WHITE,
            tooltip_rounded_radius=6,
            interactive=True,
            horizontal_grid_lines=ft.ChartGridLines(interval=1, color=ft.Colors.GREEN_300, width=0.2),
        ),
        width=500,
        height=400,
        margin=ft.margin.only(top=20, left=20, right=20),

    )

    #chart + tab
    chart_comp = ft.Container(
        ft.Tabs(
            selected_index=0,
            label_color="black",
            label_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
            indicator_color="black",
            animation_duration=1000,
            indicator_thickness=4,
            overlay_color="transparent",
            divider_color="transparent",
            tab_alignment=ft.TabAlignment.START,
            unselected_label_color=ft.Colors.GREY_600,
            tabs=[
                ft.Tab(
                    text="learning Hours",
                    content=chart
                ),
                ft.Tab(
                    text="My Courses"
                )
            ]
        ),
        expand=True,
        alignment=ft.alignment.center_left
    )

    # main content definition
    main_content = ft.Container(
        ft.Column(
            [
                ft.Container(
                    ft.Stack(
                        [
                            UIcardcontainer(
                                content=ft.Container(
                                    ft.Column(
                                        [
                                            ft.Text(value="Hello Josh!", color="black", size=35, font_family="jua"),
                                            ft.Text(value="Its good to see you again", color=ft.Colors.GREY_800,
                                                    weight=ft.FontWeight.W_100, size=12, font_family="jua")
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_AROUND
                                    ),
                                    padding=36,
                                    alignment=ft.alignment.center_left
                                ),
                                c_width=600,
                            ),
                            hi_image
                        ],
                        alignment=ft.alignment.bottom_right
                    )

                ),
                ft.Container(
                    ft.Row(
                        [
                            UIcardcontainer(
                                content=ft.Container(
                                    UIlistitem(titletext="Spanish #2", subtext="by Alexandra Velaquez",
                                               button_text="Continue")
                                ),
                                c_width=500,
                                expansion=True
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.IconButton(icon=ft.Icons.ARROW_BACK_ROUNDED, icon_color="black"),
                                        ft.IconButton(icon=ft.Icons.ARROW_FORWARD_ROUNDED, icon_color="black")
                                    ],
                                )
                            )
                        ]
                    ),
                    expand=True
                ),
                ft.Container(
                    ft.Text(
                        value="Courses",
                        color="black",
                        weight=ft.FontWeight.W_900
                    ),
                    expand=True,
                    # bgcolor="grey"
                    padding=ft.padding.only(top=14)
                ),
                tabmode
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        margin=ft.margin.only(top=30, bottom=30),
    )

    # right panel definition
    right_panel = ft.Container(
        width=600,
        height=700,
        content=ft.Column(
            [
                ft.Container(
                    ft.Row(
                        [
                            ft.Container(
                                ft.TextField(
                                    hint_text="Search anything!",
                                    focused_border_color=ft.Colors.BLACK,
                                    show_cursor=True,
                                    width=300,
                                    border_color=ft.Colors.BLACK,
                                    border_radius=14,
                                    color=ft.Colors.BLACK,
                                    cursor_color=ft.Colors.BLACK,
                                    expand=True,
                                    hint_style=ft.TextStyle(color=ft.Colors.BLACK54),
                                    prefix_icon=ft.Icon(ft.Icons.SEARCH_OUTLINED, color="black")
                                )
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color="black"),
                                        ft.Container(ft.Image(src="images/icon.png", fit=ft.ImageFit.CONTAIN),
                                                     width=24, height=24, bgcolor="gray",),
                                        ft.IconButton(icon=ft.Icons.ARROW_DROP_DOWN_OUTLINED, icon_color="black")
                                    ],spacing=10

                                )
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ),
                ft.Container(
                    ft.Row(
                        [
                            UIcardcontainer(content=ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(value="11", size=45, weight=ft.FontWeight.BOLD, font_family="jua"),
                                        ft.Column([
                                            ft.Text(value="Courses"),
                                            ft.Text(value="completed")
                                        ],
                                            spacing=0,)
                                    ]
                                ),padding=ft.padding.only(top=15,bottom=10,left=60,right=60)
                            )),
                            UIcardcontainer(content=ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(value="4", size=45, weight=ft.FontWeight.BOLD, font_family="jua"),
                                        ft.Column([
                                            ft.Text(value="Courses"),
                                            ft.Text(value="in Progress")
                                        ],
                                            spacing=0,)
                                    ]
                                ),padding=ft.padding.only(top=15,bottom=10,left=60,right=60)
                            ))
                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    margin=ft.margin.only(top=30,bottom=10),
                ),
                ft.Text(value="Your Statistics", weight=ft.FontWeight.W_900, size=24, font_family="jua"),
                ft.Container(chart_comp,width=700, height=300),
                ft.Container(
                    UIcardcontainer(
                        padding=17,
                        content=ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text(value="Learn even more!", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Column(
                                            [
                                                ft.Text(value="Unlock Premium Features", size=10,
                                                        weight=ft.FontWeight.NORMAL),
                                                ft.Text(value="only for $9.99 per month", size=10,
                                                        weight=ft.FontWeight.NORMAL),
                                            ],
                                            spacing=0,
                                        ),

                                        UIbutton("Go Premium"),

                                    ]
                                ),
                                # ft.Container(
                                #     ft.Image(src="images/actor.png", fit=ft.ImageFit.COVER),
                                #     width=64,
                                #     height=64,
                                # )
                            ]
                        )
                    ),
                    margin=ft.margin.only(top=30, bottom=30),
                )
            ],spacing=0,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )
    )

    page.add(
        ft.Container(
            ft.Row(
                [
                    menubar,
                    ft.Container(
                        ft.Row(
                            [main_content, right_panel],
                            spacing=50,
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        ),
                        margin=ft.margin.only(right=50)
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
    )


if __name__ == "__main__":
    ft.app(target=main, assets_dir="src/assets")
