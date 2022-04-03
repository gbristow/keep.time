import imp
import os
from typing import Any

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp

from kivymd.app import MDApp

from app.main_screen import TimeEventTable


class MainApp(MDApp):
    title = "keep.time"

    def build(self) -> Any:
        """
        Build the application and .kv files
        """

        Window.set_title("keep.time")
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = "Red"

        for root, _, files in os.walk(os.path.join("app")):
            for file_ in files:
                if file_.endswith(".kv") and file_ != "main.kv":
                    Builder.load_file(os.path.join(root, file_))

        return Builder.load_file(os.path.join("main.kv"))

    def on_start(self):
        self.time_events = TimeEventTable(
            use_pagination=True,
            check=True,
            column_data=[
                ("Start Time", dp(60)),
                ("Charge Code", dp(60)),
                ("Duration", dp(30)),
                ("Description", dp(60)),
            ],
        )
        self.root.ids.main.ids.table_layout.add_widget(self.time_events)

    def open_timer(self) -> None:
        # self.root.ids.timer.show()
        pass


MainApp().run()
