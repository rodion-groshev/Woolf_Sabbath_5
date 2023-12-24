from base_objects.commands_object import Commands
from utilities.input_reader import parse_input
from utilities.storage import Storage

from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit import prompt


def main():

    # main instances to save data
    book_data = Storage("temp")
    book = book_data.read_from_disk_contacts()
    notebook_data = Storage("temp_note")
    notebook = notebook_data.read_from_disk_notes()

    commands = ["add-contact", "add-phone", "add-email", "add-address", "add-birthday", "add-note", "edit-phone",
                "edit-email", "edit-address", "edit-birthday", "show-all", "show-notes", "show-contact", "show-phone",
                "show-email",
                "show-address", "show-birthday", "delete-contact", "delete-phone", "delete-email", "delete-address",
                "delete-birthday", "birthday", "exit", "help"]
    word_completer = WordCompleter(commands, ignore_case=True)

    print("Welcome to the assistant bot!")

    # main infinite loop to wait for commands, breaks after exit command
    while True:
        user_input = prompt('Enter the command: ', completer=word_completer,
                            complete_style=CompleteStyle.MULTI_COLUMN)
        # FIXME: exception if user enter no command and press enter
        command, *args = parse_input(user_input)
        data = " ".join(args)
        class_command = Commands()

        # detect command
        if command == "exit":
            print("Good bye!")
            break

        elif command == "add-contact":
            print(class_command.add_contact(data, book))
        elif command == "add-phone":
            print(class_command.add_phone(data, book))
        elif command == "add-email":
            print(class_command.add_email(data, book))
        elif command == "add-address":
            print(class_command.add_address(data, book))
        elif command == "add-birthday":
            print(class_command.add_birthday(data, book))
        elif command == "edit-phone":
            print(class_command.edit_phone(data, book))
        elif command == "edit-email":
            print(class_command.edit_email(data, book))
        elif command == "edit-address":
            print(class_command.edit_address(data, book))
        elif command == "edit-birthday":
            print(class_command.edit_birthday(data, book))
        elif command == "show-all":
            print(class_command.show_all(book))
        elif command == "show-contact":
            print(class_command.show_contact(data, book))
        elif command == "show-phone":
            print(class_command.show_phone(data, book))
        elif command == "show-email":
            print(class_command.show_email(data, book))
        elif command == "show-address":
            print(class_command.show_address(data, book))
        elif command == "show-birthday":
            print(class_command.show_birthday(data, book))
        elif command == "delete-contact":
            print(class_command.delete_contact(data, book))
        elif command == "delete-phone":
            print(class_command.delete_phone(data, book))
        elif command == "delete-email":
            print(class_command.delete_email(data, book))
        elif command == "delete-address":
            print(class_command.delete_address(data, book))
        elif command == "delete-birthday":
            print(class_command.delete_birthday(data, book))
        elif command == "birthday":
            class_command.upcoming_birthday(data, book)
        elif command == "add-note":
            print(class_command.add_new_note(data, notebook))
        elif command == "show-notes":
            print(class_command.show_all_notes(notebook))
        elif command == "help":
            class_command.help()
        else:
            print(f"Invalid command {command}.")

    book_data.save_to_disk(book)
    notebook_data.save_to_disk(notebook)


if __name__ == "__main__":
    main()
