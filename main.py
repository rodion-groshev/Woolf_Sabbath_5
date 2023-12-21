from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle

from base_commands import add_contact, add_phone, add_email, add_address, add_birthday, edit_phone, \
    edit_email, edit_address, edit_birthday, show_all, show_phone, show_email, show_address, show_birthday, \
    delete_contact, delete_phone, delete_email, delete_address, delete_birthday, upcoming_birthday
from utils.input_reader import parse_input
from book_object import AddressBook


# TO RUN FILE WRITE python main.py
# TO RUN FILE WRITE python main.py
# TO RUN FILE WRITE python main.py

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
            print(add_contact(book))
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
        elif command == "show-phone":
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


if __name__ == "__main__":
    main()
