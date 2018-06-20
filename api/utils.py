import re
from datetime import datetime


class Utils:

    @staticmethod
    def make_date_time() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def validate_number(amount):
        if not amount:
            return False

        amount_regex = re.compile("^[0-9]+$")
        if amount_regex.match(amount):
            return True

        return False
