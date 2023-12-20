from datetime import datetime
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


class AddressBook:
    pass


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    commands = ["add-contact", "add-phone", "add-email", "add-address", "add-birthday", "edit-phone", "edit-email",
                "edit-address", "edit-birthday", "show-all", "show-phone", "show-email", "show-address",
                "show-birthday", "delete-contact", "delete-phone", "delete-email", "delete-address", "delete-birthday",
                "birthday", "exit"]
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
