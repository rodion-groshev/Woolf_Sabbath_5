import re
from datetime import datetime

from base_objects.val_inp import StringValueInp


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number format")

    @staticmethod
    def validate_phone(phone):
        pattern = r"^\+?(\d{10,15})$"
        return re.match(pattern, phone) is not None


class Email(Field):
    def __init__(self, email):
        super().__init__(email)
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None


class Birthday:
    def __init__(self, value):
        if type(value) == str:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        elif type(value) == datetime:
            self.value = value

    def __str__(self):
        return str(self.value.strftime("%d.%m.%Y"))

    def __eq__(self, other):
        if type(other) == str:
            return self.value.date == datetime.strptime(other, "%d.%m.%Y").date
        elif type(other) == datetime:
            return self.value.date == other.value.date
        else:
            return False


class Address(Field):
    def __init__(self, address):
        super().__init__(address)
        if not self.validate_address(address):
            raise ValueError("The address cannot be empty.")

    @staticmethod
    def validate_address(address):
        if len(address) < 5 or len(address) > 100:
            raise ValueError("The address must contain from 5 to 100 characters.")
        if any(char in address for char in "!@#$%^&*()"):
            raise ValueError("The address contains invalid characters.")
        return address.strip()


class Note(StringValueInp):
    def __init__(self, text, tags=None):
        super().__init__(text)
        self.tags = tags or []

    def __str__(self):
        tag_string = ', '.join(self.tags)
        return f"{self.value} [Tags: {tag_string}]"

    def has_tag(self, tag):
        return tag in self.tags

    def validate(self, value):
        return value
