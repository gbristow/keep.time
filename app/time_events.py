from kivy.metrics import dp

from kivymd.uix.datatables import MDDataTable


class TimeEventsTable(MDDataTable):
    def __init__(self, **kwargs):
        use_pagination = True
        column_data = [("Start Time", dp(30))]

        super().__init__(
            use_pagination=use_pagination, column_data=column_data
        )
