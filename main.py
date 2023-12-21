from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle

from base_objects.commands_object import Commands
from utilities.input_reader import parse_input
from utilities.storage import Storage


def main():
    read_data = Storage("temp")
    book = read_data.read_from_disk()

    commands = ["add-contact", "add-phone", "add-email", "add-address", "add-birthday", "edit-phone", "edit-email",
                "edit-address", "edit-birthday", "show-all", "show-contact", "show-phone", "show-email", "show-address",
                "show-birthday", "delete-contact", "delete-phone", "delete-email", "delete-address", "delete-birthday",
                "birthday", "exit", "help"]
    word_completer = WordCompleter(commands, ignore_case=True)

    print("Welcome to the assistant bot!")
    while True:
        user_input = prompt('Enter the command: ', completer=word_completer,
                            complete_style=CompleteStyle.MULTI_COLUMN)
        command, *args = parse_input(user_input)
        class_command = Commands()

        if command == "exit":
            print("Good bye!")
            break

        elif command == "add-contact":
            print(class_command.add_contact(book))
        elif command == "add-phone":
            print(class_command.add_phone(args, book))
        elif command == "add-email":
            print(class_command.add_email(args, book))
        elif command == "add-address":
            print(class_command.add_address(args, book))
        elif command == "add-birthday":
            print(class_command.add_birthday(args, book))
        elif command == "edit-phone":
            print(class_command.edit_phone(args, book))
        elif command == "edit-email":
            print(class_command.edit_email(args, book))
        elif command == "edit-address":
            print(class_command.edit_address(args, book))
        elif command == "edit-birthday":
            print(class_command.edit_birthday(args, book))
        elif command == "show-all":
            print(class_command.show_all(book))
        elif command == "show-contact":
            print(class_command.show_contact(args, book))
        elif command == "show-phone":
            print(class_command.show_phone(args, book))
        elif command == "show-email":
            print(class_command.show_email(args, book))
        elif command == "show-address":
            print(class_command.show_address(args, book))
        elif command == "show-birthday":
            print(class_command.show_birthday(args, book))
        elif command == "delete-contact":
            print(class_command.delete_contact(args, book))
        elif command == "delete-phone":
            print(class_command.delete_phone(args, book))
        elif command == "delete-email":
            print(class_command.delete_email(args, book))
        elif command == "delete-address":
            print(class_command.delete_address(args, book))
        elif command == "delete-birthday":
            print(class_command.delete_birthday(args, book))
        elif command == "birthday":
            print(class_command.upcoming_birthday(book))
        else:
            print(f"Invalid command {command}.")

    read_data.save_to_disk(book)


if __name__ == "__main__":
    main()
