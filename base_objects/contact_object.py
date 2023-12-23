import re
from datetime import datetime


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
        if isinstance(value, str):
            self.value = datetime.strptime(value, "%d.%m.%Y")
        elif isinstance(value, datetime):
            self.value = value

    def __str__(self):
        return str(self.value.strftime("%d.%m.%Y"))

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value.date() == datetime.strptime(other, "%d.%m.%Y").date()
        elif isinstance(other, datetime):
            return self.value.date() == other.date()
        else:
            return False


class Address(Field):
    def __init__(self, address):
        super().__init__(self.validate_address(address))

    @staticmethod
    def validate_address(address):
        if len(address) < 5 or len(address) > 100:
            raise ValueError("The address must contain from 5 to 100 characters.")
        if any(char in address for char in "!@#$%^&*()"):
            raise ValueError("The address contains invalid characters.")
        return address.strip()


class Note(Field):
    def __init__(self, text, tags=None):
        super().__init__(text)
        self.tags = tags or []

    def __str__(self):
        tag_string = ', '.join(self.tags)
        return f"{self.value} [Tags: {tag_string}]"

    def has_tag(self, tag):
        return tag in self.tags

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def validate(self, value):
        return value
