import re
from datetime import datetime
from utilities.error_handler import BadPhoneNumber


class Field:
    """Field class represents fields in Records"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Name class represents Name field"""

    def __init__(self, name):
        super().__init__(name)
    # FIXME: add validation


class Tag(Field):
    """Tag class represent Tag to index Notes in field"""

    def __init__(self, tag):
        super().__init__(tag)
    # FIXME: add validation


class Note(Field):
    """Note class represent Note entered by user as field"""
    def __init__(self, value):
        super().__init__(value)
    # FIXME: add validation

class Phone(Field):
    """
    Phone class represent Phone in a field
    
    Raises
    ------
    BadPhoneNumber
        phone string is incorrect, doesn't pass validator
    """

    def __init__(self, value):
        super().__init__(value)
        if not self.validate_phone():
            # FIXME: all classes rise ValueError except this one
            raise BadPhoneNumber(value)

    def validate_phone(self):
        phone_pattern = re.compile(r'^\+38\d{9,10}$')
        return bool(re.match(phone_pattern, self.value))


class Email(Field):
    """
    Email class represent Email in a field
    
    Raises
    ------
    ValueError
        email string is incorrect, doesn't pass validator
    """

    def __init__(self, email):
        super().__init__(email)
        if not self.validate_email():
            raise ValueError("Invalid email format.")

    def validate_email(self):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, self.value) is not None


class Birthday(Field):
    """
    Birthday class represent Birthday in a field
    
    Raises
    ------
    ValueError
        birthday string is incorrect, doesn't pass validator
    """

    def __init__(self, value):
        date_format = "%d.%m.%Y"
        # FIXME: same validation style - new function
        try:
            value = datetime.strptime(value, date_format).date()
        except ValueError:
            raise ValueError("Wrong format! Date must be in format DD.MM.YYYY")
        if value.year < 1905 or value > value.today():
            raise ValueError("Incorrect date! Check your date and try again please.")
        super().__init__(value)


class Address(Field):
    """
    Address class represent Address in a field
    
    Raises
    ------
    ValueError
        Address string is incorrect, doesn't pass validator
    """

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
