import json
import re
from datetime import datetime


class Utils:

    @staticmethod
    def make_date_time() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def validate_contact(contact):
        if not contact:
            return False

        contact_regex = re.compile("^[0-9]{10,13}$")
        if contact_regex.match(contact):
            return True

        return False

    @staticmethod
    def validate_number(amount):
        if not amount:
            return False

        amount_regex = re.compile("^[0-9]+$")
        if amount_regex.match(amount):
            return True

        return False


class JSONSerializable(object):

    def to_json(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.to_json()
