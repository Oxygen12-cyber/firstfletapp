import flet as ft


def main(page: ft.Page):
    page.title="ToDo App"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.START

    task_column = ft.Column()

    def add_task(e):
        check_box =  ft.Checkbox(label=input_field.value)
        task_column.controls.append(check_box)
        input_field.value=""
        page.update()

    def clear_textfield(e):
        input_field.value=""
        page.update()



    done = ft.IconButton(icon=ft.Icons.DONE)
    cancel = ft.IconButton(icon=ft.Icons.CANCEL)
    input_field = ft.TextField(
        label="Your Task",
        on_submit=add_task,
        show_cursor=True,
       # suffix_icon=ft.Row([done, cancel],alignment=ft.MainAxisAlignment.END)
    )

    done_button = ft.IconButton(icon=ft.Icons.DONE_OUTLINE_SHARP, on_click=add_task)
    cancel_button = ft.IconButton(icon=ft.Icons.CANCEL_OUTLINED, on_click=clear_textfield)

    page.add(
        ft.Column([
            ft.Row(controls=[input_field, done_button, cancel_button], alignment=ft.MainAxisAlignment.CENTER),
            task_column,
            ft.Container(
                border_radius=10,
                width=100,
                height=100,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors.BLUE_GREY_300,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER,
                )
            )
        ])

    )

ft.app(main)