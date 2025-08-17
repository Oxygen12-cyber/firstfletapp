import flet as ft
from Course_app_dashboard import UIcardcontainer
from Course_app_dashboard import UIlistitem


def main(page: ft.Page):
    page.bgcolor = "white"
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
                            ft.Container(ft.Image(src="images/profile.png", fit=ft.ImageFit.CONTAIN),width=14,height=14,bgcolor="gray"),
                            ft.IconButton(icon=ft.Icons.ARROW_DROP_DOWN_OUTLINED, icon_color="black")
                        ],
                    )
                )
            ]
        ),
        expand=True
    )
    search_comptest=ft.Container(
        ft.Row(
            [
                            ft.Container(
                                ft.TextField(
                                    hint_text="Add a task",
                                    focused_border_color=ft.Colors.BLACK,
                                    show_cursor=True,
                                    width=300,
                                    border_color=ft.Colors.BLACK,
                                    border_radius=14,
                                    color=ft.Colors.BLACK,
                                    cursor_color=ft.Colors.BLACK,
                                    expand=True,
                                    hint_style=ft.TextStyle(color=ft.Colors.BLACK54),
                                    prefix_icon=ft.Icon(ft.Icons.SEARCH_OUTLINED, color="black"),
                                )
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color="black"),
                                        ft.Container(ft.Image(src="images/profile.png", fit=ft.ImageFit.CONTAIN),
                                                     width=14, height=14, bgcolor="gray"),
                                        ft.IconButton(icon=ft.Icons.ARROW_DROP_DOWN_OUTLINED, icon_color="black")
                                    ],
                                )
                            )
                        ]
        ),
        margin = ft.margin.only(top=30),
        expand=True
    )

    chart_comp = ft.Tabs(
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
                content=ft.Container(
                    ft.LineChart(
                        data_series=[
                            ft.LineChartData(
                                [
                                    ft.LineChartDataPoint(0,0),
                                    ft.LineChartDataPoint(1,1.5),
                                    ft.LineChartDataPoint(2,2.5),
                                    ft.LineChartDataPoint(3,1),
                                    ft.LineChartDataPoint(4,4),
                                    ft.LineChartDataPoint(5,3),
                                    ft.LineChartDataPoint(6,2)
                                ]
                            )
                        ]
                    )
                )
            )
        ]
    )

    chart = ft.Container(
        ft.LineChart(
            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(value=0,label=ft.Text("0",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=1,label=ft.Text("1",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=2,label=ft.Text("2",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=3,label=ft.Text("3",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=4,label=ft.Text("4",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=5,label=ft.Text("5",font_family="jua",color="black", size=14)),
                ]
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(value=0,label=ft.Text("mon",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=1,label=ft.Text("tue",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=2,label=ft.Text("wed",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=3,label=ft.Text("thu",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=4,label=ft.Text("fri",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=5,label=ft.Text("sat",font_family="jua",color="black", size=14)),
                    ft.ChartAxisLabel(value=6,label=ft.Text("sun",font_family="jua",color="black", size=14)),
                ]
            ),
            data_series=[
                ft.LineChartData(
                    [
                        ft.LineChartDataPoint(0,0),
                        ft.LineChartDataPoint(1,1.5),
                        ft.LineChartDataPoint(2,2.5),
                        ft.LineChartDataPoint(3,1),
                        ft.LineChartDataPoint(4,4),
                        ft.LineChartDataPoint(5,3),
                        ft.LineChartDataPoint(6,2)
                    ],
                    stroke_width=6,
                    color=ft.Colors.BLACK,
                    stroke_cap_round=True,
                    curved=True,
                    point=ft.ChartCirclePoint(color="black",stroke_width=6),
                    selected_below_line=ft.ChartPointLine(color="black",width=3)
                )
            ],
            point_line_start=0,
            point_line_end=0,
        ),
        width=600,
        height=400
    )


    page.add(chart)
ft.app(target=main)



