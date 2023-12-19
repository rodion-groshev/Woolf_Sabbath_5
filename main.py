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
    pass


class Address:
    pass


class Record:
    def __init__(self, name, phone=None, email=None, address=None, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.address = None
        self.birthday = None


class AddressBook:
    pass
