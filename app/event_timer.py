from kivy.core.window import Window

from kivymd.uix.screen import Screen
from kivymd.app import App

from app.window_handler import register_topmost, unregister_topmost


class EventTimer(Screen):
    def show(self) -> None:
        self.last_window_size = Window.size

        root = App.get_running_app().root
        root.ids.manager.current = "timer"

        Window.borderless = True
        Window.size = (300, 50)
        Window.top = 0
        Window.left = 0

        # register_topmost(Window, "keep.time")

    def hide(self) -> None:
        root = App.get_running_app().root
        root.ids.manager.current = "main"

        Window.borderless = False
        Window.size = self.last_window_size
        Window.top = 0
        Window.left = 0

        # unregister_topmost(Window, "keep.time")
