import asyncio

import flet as ft


def main(page: ft.Page) -> None:
    page.title = "Simulate BPM"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE


    page.add(
        ft.Text(
            value="Simulate BPM",
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLACK,
            size=30
        ),
        ft.Divider(height=50, color=ft.Colors.TRANSPARENT),
        ft.Icon(
            name=ft.Icons.FAVORITE,
            color=ft.Colors.PINK,
            size=250,
        ),
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        ft.Text(
            value="999 BPM",
            size=30,
            color=ft.Colors.BLACK,
            weight=ft.FontWeight.BOLD
        ),
        ft.Slider(
            label="{value}",
            divisions=100,
            width=400,
            max=100, min=0,
            active_color="#6351A2",
            thumb_color="#6351A2",
            inactive_color=ft.Colors.GREY,
            on_change=lambda e: [
                setattr(e.control.parent.controls[4], "value", int(e.control.value) * 2 + 14),
                setattr(e.control.parent.controls[2], "size", int(e.control.value) + 100),
                e.page.update()
            ]
        )
    )

    async def scaling():
        while True:
            page.controls[2].scale = 1.3
            page.controls[2].animate_scale = 1000 #ft.Animation(duration=3000, curve=ft.AnimationCurve.EASE_OUT)
            page.update()
            await asyncio.sleep(1)
            page.controls[2].scale = None
            page.controls[2].animate_scale = 1000 #ft.Animation(duration=3000, curve=ft.AnimationCurve.EASE_IN)
            page.update()
            await asyncio.sleep(1)


    page.run_task(scaling)

ft.app(target=main)
