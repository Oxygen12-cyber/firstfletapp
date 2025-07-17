import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#1e1e1e"
    page.padding = 30

    glass_card = ft.Container(
        content=ft.Column([
            ft.Text("Glassmorphism ✨", size=22, weight=ft.FontWeight.BOLD, color="white"),
            ft.Text("A modern glass-style UI using Flet", color="white70"),
        ]),
        width=300,
        height=150,
        bgcolor=ft.Colors.with_opacity(0.15, "white"),
        border_radius=20,
        padding=20,
        border=ft.border.all(1, "white24"),
        shadow=ft.BoxShadow(blur_radius=15, color="black45"),
        # Add this to simulate blur (Flet hack: not true blur)
    )

    page.add(glass_card)

ft.app(target=main)
