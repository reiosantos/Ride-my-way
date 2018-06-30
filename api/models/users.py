from typing import List

from api.utils.utils import JSONSerializable, Utils


class Users:
    class UserModel(JSONSerializable):
        def __init__(self, full_name=None, contact=None, username=None,
                     password=None, user_type=None):
            self.user_id = Utils.generate_user_id()
            self.registration_date = Utils.make_date_time()

            self.full_name = full_name
            self.username = username
            self.contact = contact
            self.password = password
            self.user_type = user_type

    users: List[UserModel] = []

    @staticmethod
    def create_user(full_name=None, contact=None, username=None,
                    password=None, user_type="passenger") -> UserModel or None:

        user = Users.UserModel(full_name, contact, username, password, user_type)
        Users.users.append(user)
        return user

    @classmethod
    def get_all_users(cls) -> List[UserModel]:
        return cls.users

    @classmethod
    def find_user(cls, user_id) -> UserModel or None:
        try:
            user_id = int(user_id)
        except ValueError:
            return None

        for user in cls.users:
            if user.user_id == user_id:
                return user
        return None

    @classmethod
    def update_user(cls, user_id=None, full_name=None, contact=None, username=None,
                    password=None, user_type="passenger") -> bool:

        user = cls.find_user(user_id)
        if not user:
            return False
        index = cls.users.index(user)

        user.user_type = user_type
        if password:
            user.password = password
        user.full_name = full_name
        user.contact = contact
        user.username = username

        cls.users.insert(index, user)
        return True

    @classmethod
    def delete_user(cls, user_id) -> bool:

        user = cls.find_user(user_id)
        if not user:
            return False

        cls.users.remove(user)
        return True
