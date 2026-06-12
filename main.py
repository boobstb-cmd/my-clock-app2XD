import flet as ft
import time
import threading

def main(page: ft.Page):
    page.title = "Мои Часы"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    clock_text = ft.Text(value="00:00:00", size=60, weight=ft.FontWeight.BOLD, color="white")
    page.add(clock_text)

    def update_clock():
        while True:
            clock_text.value = time.strftime("%H:%M:%S")
            page.update()
            time.sleep(1)

    thread = threading.Thread(target=update_clock, daemon=True)
    thread.start()

ft.app(target=main)
