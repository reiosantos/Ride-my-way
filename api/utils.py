from datetime import datetime


class Utils:

    @staticmethod
    def make_date_time() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
