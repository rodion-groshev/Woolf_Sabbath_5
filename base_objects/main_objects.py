import re
from datetime import datetime
from utilities.error_handler import BadPhoneNumber, BadEmailFormat, EmptyNameFormat


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        if name == "":
            raise EmptyNameFormat
        super().__init__(name)


class Tag(Field):
    def __init__(self, tag):
        super().__init__(tag)


class Note(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_phone():
            raise BadPhoneNumber(value)

    def validate_phone(self):
        phone_pattern = re.compile(r"^\+38\d{9,10}$")
        return bool(re.match(phone_pattern, self.value))


class Email(Field):
    def __init__(self, email):
        super().__init__(email)
        if not self.validate_email():
            raise BadEmailFormat(email)

    def validate_email(self):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, self.value) is not None


class Birthday(Field):
    def __init__(self, value):
        date_format = "%d.%m.%Y"
        try:
            value = datetime.strptime(value, date_format).date()
        except ValueError:
            raise ValueError("Wrong format! Date must be in format DD.MM.YYYY")
        if value.year < 1905 or value > value.today():
            raise ValueError("Incorrect date! Check your date and try again please.")
        super().__init__(value)


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
