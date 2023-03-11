from records.record import Record

class Interface:
    def __init__(self):
        self._main_df = Record().dataframe

    def add_record(self, record: Record):
        pass

    def get_record(self, condition):
        pass

    def get_avg(self, condition):
        pass

    def get_max(self, condition):
        pass

    def get_max(self, condition):
        pass
