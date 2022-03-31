import imp
import os
from typing import Any

from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp

class MainApp(MDApp):
    title = "keep.time"

    def build(self) -> Any:
        """
        Build the application and .kv files
        """

        Window.set_title("keep.time")
        

        for root, _, files in os.walk(os.path.join("app")):
            for file_ in files:
                if file_.endswith(".kv") and file_ != "main.kv":
                    Builder.load_file(os.path.join(root, file_))

        return Builder.load_file(os.path.join("main.kv"))

    def on_start(self):
        pass

    def open_timer(self) -> None:
        self.root.ids.timer.show()
        print("Open Timer")


MainApp().run()
