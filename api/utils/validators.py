import re


class Validators:

    @staticmethod
    def validate_contact(contact) -> bool:
        if not contact:
            return False

        contact_regex = re.compile("^[0-9]{10,13}$")
        if contact_regex.match(contact):
            return True

        return False

    @staticmethod
    def validate_number(amount) -> bool:
        if not amount:
            return False
        amount_regex = re.compile("^[0-9]+$")
        if amount_regex.match(amount):
            return True

        return False

    @staticmethod
    def validate_email(email) -> bool:
        pattern = re.compile("^[A-Za-z0-9.+_-]+@[A-Za-z0-9._-]+\.[a-zA-Z]*$")
        if not pattern.match(email):
            return False
        return True

