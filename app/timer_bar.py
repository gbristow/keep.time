from datetime import datetime
from typing import Union

from kivy.clock import Clock
from kivy.app import App

from kivymd.uix.boxlayout import BoxLayout


class TimerBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.start_time: Union[datetime, None] = None

    def charge_code_selected(self, charge_code) -> None:
        print(charge_code)

    def start_timer(self) -> None:
        self.start_time = datetime.now()
        Clock.schedule_interval(self.count_timer, 1)

    def stop_timer(self) -> None:
        assert self.start_time is not None
        elapsed_time = datetime.now() - self.start_time
        self.start_time = None

        app = App.get_running_app()
        app.root.ids.main.ids.timer_bar.ids.timer.text = "00:00:00"

        Clock.unschedule(self.count_timer)

    def count_timer(self, dt) -> None:
        assert self.start_time is not None
        elapsed_time = datetime.now() - self.start_time
        
        app = App.get_running_app()
        app.root.ids.main.ids.timer_bar.ids.timer.text = str(elapsed_time)
