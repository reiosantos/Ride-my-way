
from api.utils import Utils, JSONSerializable


class UserModel(JSONSerializable):
    def __init__(self, user_id=1, full_name=None, contact=0, username=None, password=None, user_type=0):
        self.user_id = user_id
        self.full_name = full_name
        self.username = username
        self.contact = contact
        self.registration_date = Utils.make_date_time()
        self.password = password
        self.user_type = user_type
