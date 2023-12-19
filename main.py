from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name:
    pass


class Phone:
    pass


class Email:
    pass


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

class Address:
    pass


class Record:
    def __init__(self, name, phone=None, email=None, address=None, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.address = None
        self.birthday = None
        
    if phone:
        self.add_phone(phone)
    if email:
        self.add_email(email)
    if address:
        self.add_address(address)
    if birthday:
        self.add_birthday(birthday)

    @input_error
    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    @input_error
    def add_email(self, email):
        new_email = Field(email)
        self.emails.append(new_email)

class AddressBook:
    pass
