from datetime import datetime
from features.error_handler import BadBirthdayFormat, PhoneNumberIsMissing, ValidationException
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.completion import WordCompleter


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

    @input_error
    def add_address(self, address):
        self.address = Field(address)

    @input_error
    def add_birthday(self, birthday):
        self.birthday = Field(birthday)
    
    @input_error
    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
        else:
            raise PhoneNumberIsMissing("Phone number not found in the record.")
    
    @input_error
    def edit_email(self, old_email, new_email):
        if old_email in self.emails:
            index = self.emails.index(old_email)
            self.emails[index] = new_email
        else:
            raise ValidationException("Email not found in the record.")

    @input_error
    def edit_address(self, new_address):
        self.address = Field(new_address)

    @input_error
    def edit_birthday(self, new_birthday):
        if isinstance(new_birthday, Birthday):
            self.birthday = new_birthday
        else:
            raise BadBirthdayFormat("Invalid birthday format. Expected format: dd/mm/yyyy.")
        


class AddressBook:
    def __init__(self):
        self.contacts = {}
        
    def add_contact(self, name, address, phone, email, birthday):
        contact = Record(name)
        contact.add_address(address)
        contact.add_phone(phone)
        contact.add_email(email)
        contact.add_birthday(birthday)
        self.contacts[name] = contact

    def view_contact(self, name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print(f"Contact '{name}' not found.")

    def find_contact(self, query):
        matches = [name for name in self.contacts if re.search(query, name, re.IGNORECASE)]
        if matches:
            print(f"\nMatching contacts for '{query}':")
            for match in matches:
                print(self.contacts[match])
        else:
            print(f"No contacts found for '{query}'.")

    def show_all(self):
        if self.contacts:
            print("\nAll Contacts:")
            for name, contact in self.contacts.items():
                print(f"\n{name}:\n{contact}")
        else:
            print("No contacts in the address book.")

    def show_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"\n{name}:\n{contact}")
        else:
            print(f"Contact '{name}' not found.")

    def show_phone(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            if contact.phones:
                print(f"\n{name}'s Phone Numbers:")
                for phone in contact.phones:
                    print(phone)
            else:
                print(f"{name} has no phone numbers.")
        else:
            print(f"Contact '{name}' not found.")

    def show_email(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            if contact.email:
                print(f"\n{name}'s Email:")
                print(contact.email)
            else:
                print(f"{name} has no email address.")
        else:
            print(f"Contact '{name}' not found.")

    def show_address(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            if contact.address:
                print(f"\n{name}'s Address:")
                print(contact.address)
            else:
                print(f"{name} has no address.")
        else:
            print(f"Contact '{name}' not found.")

    def show_birthday(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            if contact.birthday:
                print(f"\n{name}'s Birthday:")
                print(contact.birthday)
            else:
                print(f"{name} has no birthday.")
        else:
            print(f"Contact '{name}' not found.")

    def upcoming_birthday(self, days):
        today = datetime.now()
        upcoming_birthdays = []

        for name, contact in self.contacts.items():
            if contact.birthday:
                birthday = contact.birthday.date
                next_birthday = datetime(today.year, birthday.month, birthday.day)

                if next_birthday < today:
                    next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

                days_until_birthday = (next_birthday - today).days

                if 0 < days_until_birthday <= days:
                    upcoming_birthdays.append((name, contact.birthday))

        return upcoming_birthdays

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def upcoming_birthdays(self, days):
        today = datetime.now()
        upcoming_birthdays = []

        for name, contact in self.contacts.items():
            birthday = contact.birthday.date
            next_birthday = datetime(today.year, birthday.month, birthday.day)

            if next_birthday < today:
                next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

            days_until_birthday = (next_birthday - today).days

            if 0 < days_until_birthday <= days:
                upcoming_birthdays.append((name, contact.birthday))

        return upcoming_birthdays


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_phone(args, book):
    name, phone = args
    record = book.find(name)
    record.add_phone(phone)
    return f"Phone: {phone} added to contact {name}."


def add_email(args, book):
    name, email = args
    record = book.find(name)
    record.add_email(email)
    return f"Email: {email} added to contact {name}."


def add_address(args, book):
    name, address = args
    record = book.find(name)
    record.add_address(address)
    return f"Address: {Address} added to contact {name}."


def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    record.add_birthday(birthday)
    return f"Birthday: {birthday} added to contact {name}."


def edit_phone(args, book):
    name, old_phone, new_phone = args
    if name in book:
        record = book.find(name)
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        return "Contact not found"


def edit_email(args, book):
    name, old_email, new_email = args
    if name in book:
        record = book.find(name)
        record.edit_email(old_email, new_email)
        return "Contact updated."
    else:
        return "Contact not found"


def edit_address(args, book):
    name, address = args
    if name in book:
        record = book.find(name)
        record.edit_address(address)
        return "Contact updated."
    else:
        return "Contact not found"


def edit_birthday(args, book):
    name, birthday = args
    if name in book:
        record = book.find(name)
        record.edit_birthday(birthday)
        return "Contact updated."
    else:
        return "Contact not found"


def show_all(book):
    return "\n".join(f"{value}" for name, value in book.items())


def show_phone(args, book):
    name = args[0]
    return book.show_phone(name)


def show_email(args, book):
    name = args[0]
    return book.show_email(name)


def show_address(args, book):
    name = args[0]
    return book.show_address(name)


def show_birthday(args, book):
    name = args[0]
    return book.show_birthday(name)


def delete_contact(args, book):
    name = args[0]
    return book.delete_contact(name)


def delete_phone(args, book):
    name, phone = args
    record = book.find(name)
    return record.delete_phone(phone)


def delete_email(args, book):
    name, email = args
    record = book.find(name)
    return record.delete_email(email)


def delete_address(args, book):
    name, address = args
    record = book.find(name)
    return record.delete_email(address)


def delete_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    return record.delete_email(birthday)


def upcoming_birthday(book):
    return book.upcoming_birthday()


def main():
    book = AddressBook()
    commands = ["add-contact", "add-phone", "add-email", "add-address", "add-birthday", "edit-phone", "edit-email",
                "edit-address", "edit-birthday", "show-all", "show-phone", "show-email", "show-address",
                "show-birthday", "delete-contact", "delete-phone", "delete-email", "delete-address", "delete-birthday",
                "birthday", "exit", "help"]
    word_completer = WordCompleter(commands, ignore_case=True)

    print("Welcome to the assistant bot!")
    while True:
        user_input = prompt('Enter the command: ', completer=word_completer, complete_style=CompleteStyle.MULTI_COLUMN)
        command, *args = parse_input(user_input)

        if command == "exit":
            print("Good bye!")
            break
        elif command == "add-contact":
            print(add_contact(args, book))
        elif command == "add-phone":
            print(add_phone(args, book))
        elif command == "add-email":
            print(add_email(args, book))
        elif command == "add-address":
            print(add_address(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "edit-phone":
            print(edit_phone(args, book))
        elif command == "edit-email":
            print(edit_email(args, book))
        elif command == "edit-address":
            print(edit_address(args, book))
        elif command == "edit-birthday":
            print(edit_birthday(args, book))
        elif command == "show-all":
            print(show_all(book))
        elif command == "show_phone":
            print(show_phone(book))
        elif command == "show-email":
            print(show_email(book))
        elif command == "show-address":
            print(show_address(book))
        elif command == "show-birthday":
            print(show_birthday(book))
        elif command == "delete-contact":
            print(delete_contact(args, book))
        elif command == "delete-phone":
            print(delete_phone(args, book))
        elif command == "delete-email":
            print(delete_email(args, book))
        elif command == "delete-address":
            print(delete_address(args, book))
        elif command == "delete-birthday":
            print(delete_birthday(args, book))
        elif command == "birthday":
            print(upcoming_birthday(book))
        else:
            print(f"Invalid command {command}.")
