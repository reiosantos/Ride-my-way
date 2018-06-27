import json
import re
from datetime import datetime


class Utils:

    @staticmethod
    def make_date_time() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class JSONSerializable(object):

    def to_json(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.to_json()
