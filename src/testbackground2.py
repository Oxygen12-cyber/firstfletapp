import flet as ft


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.min_width = 1000
    page.min_height = 1000
    # page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.title = "Background2"

    #emailbox
    email_box = ft.Container(
        ft.TextField(
            label="Your Email",
            border_radius=12,
            width=300,
            border_color="#ffffff",
            label_style=ft.TextStyle(color=ft.Colors.WHITE30),
            hint_style=ft.TextStyle(color=ft.Colors.WHITE30),
            text_style=ft.TextStyle(color=ft.Colors.WHITE)
        ),
        margin=ft.margin.only(top=20)
    )
    #password box
    pass_box = ft.Container(
        ft.TextField(
            label="Your Password",
            border_radius=12,
            width=300,
            border_color="#ffffff",
            label_style=ft.TextStyle(color=ft.Colors.WHITE30),
            text_style=ft.TextStyle(color=ft.Colors.WHITE),
            password=True,
        ),
        margin=ft.margin.only(top=6)
    )
    #signinbutton
    sign_in = ft.Container(
        ft.Button(
            text="Sign in",
            icon="sign-in",
            style=ft.ButtonStyle(bgcolor="#fffbff9", shape=ft.RoundedRectangleBorder(4), color="purple")
        ),
        margin=ft.margin.only(top=12),
        width=80
    )
    #centerblock
    center_block = ft.Container(
        ft.Container(
            ft.Column(
                controls=[
                    ft.Text(
                        "Login",
                        color="white",
                        weight=ft.FontWeight.BOLD,
                        size=26
                    ),
                    ft.Container(email_box),
                    ft.Container(pass_box),
                    ft.Container(sign_in)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            width=500,
            height=600,
            margin=ft.margin.only(top=140),
            bgcolor="#fffbff9",
            border_radius=18,
            blur=ft.Blur(2, 2, ft.BlurTileMode.MIRROR),
            border=ft.border.all(3, "#ffffff0"),
            alignment=ft.alignment.center
        ),
        alignment=ft.alignment.center
    )
    #mainbody
    body = ft.Container(
        ft.Stack(
            [
                ft.Image(src="images/moonbg.jpg", fit=ft.ImageFit.COVER),
                center_block,
            ],
        ),
        alignment=ft.alignment.center
    )

    page.add(
        body,
    )


ft.app(main)
