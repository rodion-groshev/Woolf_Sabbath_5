from utilities.color_cmd import Color
from base_objects.commands_object import Commands
from utilities.input_reader import parse_input
from utilities.storage import Storage

from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit import prompt


def main():
    # Initializing storage for contacts and notes from files
    book_data = Storage("temp")
    book = book_data.read_from_disk_contacts()
    notebook_data = Storage("temp_note")
    notebook = notebook_data.read_from_disk_notes()

    # List of available commands
    commands = [
        "add-contact",
        "add-phone",
        "add-email",
        "add-address",
        "add-birthday",
        "add-note",
        "edit-phone",
        "edit-email",
        "edit-address",
        "edit-birthday",
        "edit-note",
        "delete-note",
        "show-all",
        "show-notes",
        "show-contact",
        "show-phone",
        "show-email",
        "show-address",
        "show-birthday",
        "show-note",
        "delete-contact",
        "delete-phone",
        "delete-email",
        "delete-address",
        "delete-birthday",
        "birthday",
        "exit",
        "help",
        "change-color",
    ]
    word_completer = WordCompleter(commands, ignore_case=True)
    color = Color()

    color.print_text(
        "\t\t\t\t\t\t\t******************************************************\n"
    )
    color.print_text(
        "\t\t\t\t\t\t\t*       Welcome to your personal Assistant Bot!      *\n"
    )
    color.print_text(
        "\t\t\t\t\t\t\t******************************************************\n"
    )

    while True:
        # Input from the user
        user_input = prompt(
            color.print_text("\n---> Enter the command: "),
            completer=word_completer,
            complete_style=CompleteStyle.MULTI_COLUMN,
        )
        command, *args = parse_input(user_input)
        data = " ".join(args)
        class_command = Commands()
        # Main commands
        if command == "exit":
            color.print_text("Good bye!")
            break
        elif command == "add-contact":
            color.print_text(class_command.add_contact(data, book))
        elif command == "add-phone":
            color.print_text(class_command.add_phone(data, book))
        elif command == "add-email":
            color.print_text(class_command.add_email(data, book))
        elif command == "add-address":
            color.print_text(class_command.add_address(data, book))
        elif command == "add-birthday":
            color.print_text(class_command.add_birthday(data, book))
        elif command == "edit-phone":
            color.print_text(class_command.edit_phone(data, book))
        elif command == "edit-email":
            color.print_text(class_command.edit_email(data, book))
        elif command == "edit-address":
            color.print_text(class_command.edit_address(data, book))
        elif command == "edit-birthday":
            color.print_text(class_command.edit_birthday(data, book))
        elif command == "show-all":
            color.print_text(class_command.show_all(book))
        elif command == "show-contact":
            color.print_text(class_command.show_contact(data, book))
        elif command == "show-phone":
            color.print_text(class_command.show_phone(data, book))
        elif command == "show-email":
            color.print_text(class_command.show_email(data, book))
        elif command == "show-address":
            color.print_text(class_command.show_address(data, book))
        elif command == "show-birthday":
            color.print_text(class_command.show_birthday(data, book))
        elif command == "delete-contact":
            color.print_text(class_command.delete_contact(data, book))
        elif command == "delete-phone":
            color.print_text(class_command.delete_phone(data, book))
        elif command == "delete-email":
            color.print_text(class_command.delete_email(data, book))
        elif command == "delete-address":
            color.print_text(class_command.delete_address(data, book))
        elif command == "delete-birthday":
            color.print_text(class_command.delete_birthday(data, book))
        elif command == "birthday":
            class_command.upcoming_birthday(data, book)
        elif command == "add-note":
            color.print_text(class_command.add_new_note(data, notebook))
        elif command == "show-notes":
            color.print_text(class_command.show_all_notes(notebook))
        elif command == "show-note":
            color.print_text(class_command.show_note(data, notebook))
        elif command == "edit-note":
            color.print_text(class_command.edit_note(data, notebook))
        elif command == "delete-note":
            color.print_text(class_command.delete_note(data, notebook))
        elif command == "help":
            class_command.help()
        elif command == "change-color":
            color.print_text(class_command.change_bot_color(data, color))
        else:
            color.print_text(f"Invalid command {command}.")

    book_data.save_to_disk(book)
    notebook_data.save_to_disk(notebook)


if __name__ == "__main__":
    main()
