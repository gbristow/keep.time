from cgitb import text
from datetime import datetime, timedelta

from typing import Union

from kivy.clock import Clock
from kivy.app import App

from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


def strfdelta(tdelta: timedelta, fmt: str) -> str:
    d = {"d": tdelta.days}
    d["H"], rem = divmod(tdelta.seconds, 3600)
    d["M"], d["S"] = divmod(rem, 60)

    d["H"] = pad_time(d["H"])
    d["M"] = pad_time(d["M"])
    d["S"] = pad_time(d["S"])

    return fmt.format(**d)


def pad_time(time: Union[str, float, int], padding=2) -> str:
    time_str = str(time)

    for i in range(0, padding - len(str(time))):
        time_str = "0" + time_str

    return time_str


class TimerBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.start_time: Union[datetime, None] = None

    def charge_code_selected(self, charge_code) -> None:
        print(charge_code)

    def start_timer(self) -> None:
        app = App.get_running_app()
        app.root.ids.main.ids.timer_bar.ids.timer.text = "00:00:00"
        
        if app.root.ids.main.ids.timer_bar.ids.charge_code.text == "Select Charge Code":
            self.select_charge_code_alert()
            return

        self.start_time = datetime.now()
        Clock.schedule_interval(self.count_timer, 1)

    def stop_timer(self) -> None:
        assert self.start_time is not None
        elapsed_time = strfdelta(
            datetime.now() - self.start_time, "{H}:{M}:{S}"
        )

        app = App.get_running_app()
        app.root.ids.main.ids.timer_bar.ids.timer.text = "00:00:00"

        assert self.start_time is not None
        row_data = app.time_events.row_data
        
        start_time = self.start_time.strftime("%m/%d/%y, %H:%M:%S")
        charge_code = app.root.ids.main.ids.timer_bar.ids.charge_code.text
        row_data.append((start_time, "", elapsed_time, charge_code))

        Clock.unschedule(self.count_timer)
        self.start_time = None

    def count_timer(self, dt) -> None:
        assert self.start_time is not None
        elapsed_time = strfdelta(
            datetime.now() - self.start_time, "{H}:{M}:{S}"
        )

        app = App.get_running_app()
        app.root.ids.main.ids.timer_bar.ids.timer.text = elapsed_time

    def select_charge_code_alert(self) -> None:
        dialog = MDDialog(
            text="Please select charge code",
        )
        dialog.open()
