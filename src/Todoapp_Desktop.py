import flet as ft


def main(page: ft.Page):
    page.title = "CHATGPT ToDo PC APP"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#FF2D2D30"
    page.fonts = {"Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Medium.ttf"}
    page.theme = ft.Theme(font_family="Kanit")

    task_column = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        alignment=ft.MainAxisAlignment.START,
    )

    def focus_mode(e):
        done_button.visible = True
        cancel_button.visible = True
        done_button.update()
        cancel_button.update()

    def add_task(e):
        if not box_input.value == "":
            check_box = ft.Checkbox(
                label=box_input.value,
                label_style=ft.TextStyle(color="white", size=24, weight=ft.FontWeight.NORMAL),
                hover_color=ft.Colors.GREY_700,
                active_color=ft.Colors.GREY_300,
                check_color=ft.Colors.GREY_800,
            )
            task_column.controls.append(check_box)
            box_input.value = ""
            page.update()

    def cancel_value(e):
        box_input.value = ""
        box_input.update()

    def onblur(e):
        box_input.value = ""
        done_button.visible = False
        cancel_button.visible = False
        page.update()

    done_button = ft.IconButton(icon=ft.Icons.DONE, visible=False, on_click=add_task, tooltip="save task", hover_color=ft.Colors.BLUE_GREY_300)
    cancel_button = ft.IconButton(icon=ft.Icons.CANCEL, visible=False, on_click=cancel_value, tooltip="delete task", hover_color=ft.Colors.BLUE_GREY_300)
    box_input = ft.TextField(
        label="Add a task",
        on_focus=focus_mode,
        focused_border_color=ft.Colors.WHITE,
        show_cursor=True,
        width=300,
        border_color=ft.Colors.WHITE,
        border_radius=14,
        on_submit=add_task,
        on_blur=onblur,
        color=ft.Colors.WHITE,
        cursor_color=ft.Colors.WHITE,
        expand=True,
        label_style=ft.TextStyle(color=ft.Colors.WHITE54),
        # on_tap_outside=cancel_value,
        suffix_icon=ft.Container(
            ft.Row(
                [done_button, cancel_button],
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER,
                tight=True
            )
        )
    )

    page.add(
        ft.Container(
            bgcolor="#FF2D2D30",
            content=ft.Column(
                [
                    ft.Container(
                        ft.Text(
                            "My To-Dos 📝",
                            text_align=ft.alignment.center_right,
                            size=30,
                            color=ft.Colors.WHITE
                        ), margin=ft.margin.only(left=20, top=40)
                    ),
                    ft.Container(
                        ft.Row([
                            ft.Container(
                                box_input,
                                width=330,
                                height=80,
                                bgcolor=ft.Colors.BLACK26,
                                border_radius=28,
                                alignment=ft.alignment.center,
                                shadow=ft.BoxShadow(
                                    blur_radius=15,
                                    spread_radius=1,
                                    offset=ft.Offset(0, 0),
                                    color=ft.Colors.BLACK12,
                                    blur_style=ft.ShadowBlurStyle.SOLID,
                                )
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER),
                        margin=ft.margin.only(top=40),
                    ),
                    ft.Container(
                        ft.Row([
                            ft.Container(
                                task_column,
                                padding=ft.padding.only(top=20, left=20),
                                # width=380,
                                expand=True,
                                margin=ft.margin.only(left=20, right=20, top=40),
                                height=600,
                                bgcolor=ft.Colors.BLACK26,
                                border_radius=24,
                                shadow=ft.BoxShadow(
                                    blur_radius=15,
                                    spread_radius=3,
                                    offset=ft.Offset(0, 0),
                                    color=ft.Colors.BLACK12,
                                    blur_style=ft.ShadowBlurStyle.SOLID,
                                )
                            ),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        margin=ft.margin.only(top=10)
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            )
        )
    )


ft.app(main)
