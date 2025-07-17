import flet as ft
from flet.core.webview import WebView


def main(page: ft.Page):
    page.title = "CHATGPT ToDo Mobile Version"
    print('App Reloading')
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def focus_mode(e):
        if e.data == "true":
            box_input.suffix_icon.visible = True
            page.update()
            print(e.data)
        else:
            box_input.suffix_icon.visible = False
            page.update()

    task_column = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        alignment=ft.MainAxisAlignment.START,
    )

    def add_task(e):
        check_box = ft.Checkbox(
            label=box_input.value,
            label_style=ft.TextStyle(color="white"),
            active_color=ft.Colors.GREY_300,
            check_color=ft.Colors.GREY_800,
        )
        task_column.controls.append(check_box)
        box_input.value = ""
        page.update()

    def cancel_value(e):
        page.update()

    done_button = ft.IconButton(icon=ft.Icons.DONE, on_click=add_task)
    cancel_button = ft.IconButton(icon=ft.Icons.CANCEL, on_click=cancel_value)
    box_input = ft.TextField(
        label="Add a task",
        on_focus=focus_mode,
        focused_border_color=ft.Colors.WHITE,
        show_cursor=True,
        width=300,
        border_color=ft.Colors.WHITE,
        border_radius=14,
        on_submit=add_task,
        color=ft.Colors.WHITE,
        cursor_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE24),
        suffix_icon=ft.Row(
            [done_button, cancel_button],
            visible=False,
            alignment=ft.MainAxisAlignment.END)
    )

    page.add(
        ft.Container(
            bgcolor=ft.Colors.GREY_400,
            height=800,
            width=400,
            alignment=ft.alignment.center,
            content=ft.Card(
                ft.Column([
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
                                width=320,
                                height=80,
                                bgcolor=ft.Colors.BLACK26,
                                border_radius=26,
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
                                width=380,
                                height=500,
                                bgcolor=ft.Colors.BLACK12,
                                border_radius=24,
                                shadow=ft.BoxShadow(
                                    blur_radius=15,
                                    spread_radius=1,
                                    offset=ft.Offset(0, 0),
                                    color=ft.Colors.BLACK12,
                                    blur_style=ft.ShadowBlurStyle.SOLID,
                                )
                            ),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        margin=ft.margin.only(top=10)
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                elevation=2,
                color=ft.Colors.BLACK54,
            )
        )
    )


ft.app(target=main)
