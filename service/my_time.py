from datetime import datetime

# TODO not used
class Time:

    @staticmethod
    def get_seconds_since_midnight():
        now = datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = now - midnight
        return int(delta.total_seconds())
