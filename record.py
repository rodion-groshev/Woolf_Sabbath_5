class Name():
    pass

class Phone():
    pass


class Email():
    pass

class Birthday():
    pass

class Address():
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, date_str):
        self.birthday = Birthday(date_str)

    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, address):
        self.address = Address(address)

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone: {', '.join(map(str, self.phones))}\nEmail: {self.email}\nBirthday: {self.birthday}"
        self.address = Address(address)
