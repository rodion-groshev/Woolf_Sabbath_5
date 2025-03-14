from colorama import Fore

from utilities.error_handler import (
    input_error,
    EmptyFieldsException,
)
from base_objects.record_object import Record, NoteRecord
from utilities.help_message import help_message
from utilities.birtday_output import birthday_output


class Commands:
    @input_error
    def add_contact(self, name, book):
        record = Record(name)
        phone = input("Enter the phone: ")
        if phone:
            record.add_phone_record(phone)
        email = input("Enter email address: ")
        if email:
            record.add_email_record(email)
        address = input("Enter the address: ")
        if address:
            record.add_address_record(address)
        birthday = input("Enter a birthday: ")
        if birthday:
            record.add_birthday_record(birthday)

        if not phone and not email and not address and not birthday:
            raise EmptyFieldsException

        book.add_contact_book(record)
        return f"Contact {name} added successfully."

    @input_error
    def add_phone(self, name, book):
        record = book.find(name)
        phone = input("Enter the phone number: ")
        record.add_phone_record(phone)
        return f"Phone: {phone} added to contact {name}."

    @input_error
    def add_email(self, name, book):
        record = book.find(name)
        email = input("Enter email address: ")
        record.add_email_record(email)
        return f"Email: {email} added to contact {name}."

    @input_error
    def add_address(self, name, book):
        record = book.find(name)
        address = input("Enter the address: ")
        record.add_address_record(address)
        return f"Address: {address} added to contact {name}."

    @input_error
    def add_birthday(self, name, book):
        record = book.find(name)
        birthday = input("Enter the birthday: ")
        record.add_birthday_record(birthday)
        return f"Birthday: {birthday} added to contact {name}."

    @input_error
    def edit_phone(self, name, book):
        record = book.find(name)
        old_phone = input("Enter the old phone number: ")
        new_phone = input("Enter the new phone number: ")
        record.edit_phone_record(old_phone, new_phone)
        return f"{name}'s phone updated. New phone: {new_phone}"

    @input_error
    def edit_email(self, name, book):
        record = book.find(name)
        old_email = input("Enter the old email address: ")
        new_email = input("Enter the new email address: ")
        record.edit_email_record(old_email, new_email)
        return f"{name}'s email updated. New email: {new_email}"

    @input_error
    def edit_address(self, name, book):
        record = book.find(name)
        address = input("Enter the address: ")
        record.edit_address_record(address)
        return f"{name}'s address updated. New address: {address}"

    @input_error
    def edit_birthday(self, name, book):
        record = book.find(name)
        birthday = input("Enter the birthday date: ")
        record.edit_birthday_record(birthday)
        return f"{name}'s birthday updated. New birthday: {birthday}"

    @input_error
    def show_all(self, book):
        return f"All contacts in your AddressBook:\n\n{book.show_all_book()}"

    @input_error
    def show_contact(self, name, book):
        return book.show_contact_book(name)

    @input_error
    def show_phone(self, name, book):
        return f"{name}'s phone(s): {book.show_phone_book(name)}"

    @input_error
    def show_email(self, name, book):
        return book.show_email_book(name)

    @input_error
    def show_address(self, name, book):
        return book.show_address_book(name)

    @input_error
    def show_birthday(self, name, book):
        return book.show_birthday_book(name)

    @input_error
    def delete_contact(self, name, book):
        return book.delete_contact_book(name)

    @input_error
    def delete_phone(self, name, book):
        record = book.find(name)
        phone = input("Enter the phone number to delete: ")
        record.delete_phone_record(phone)
        return f"Phone number {phone} deleted for contact {name}."

    @input_error
    def delete_email(self, name, book):
        record = book.find(name)
        email = input("Enter the email to delete: ")
        record.delete_email_record(email)
        return f"Email {email} deleted for contact {name}."

    @input_error
    def delete_address(self, name, book):
        record = book.find(name)
        record.delete_address_record()
        return f"Address deleted for contact {name}."

    @input_error
    def delete_birthday(self, name, book):
        record = book.find(name)
        record.delete_birthday_record()
        return f"Birthday deleted for contact {name}."

    @input_error
    def upcoming_birthday(self, days, book):
        birthday_output(book.birthday_func(int(days)))

    @input_error
    def add_new_note(self, data, notebook):
        note_input = input("Enter the note: ")
        note_record = NoteRecord(data)
        note_record.add_note_record(note_input)
        notebook.add_note(note_record)
        return f"Note {data} added successfully."

    @input_error
    def show_all_notes(self, notebook):
        return notebook.show_all_notes()

    @input_error
    def show_note(self, data, notebook):
        note_record = notebook.find(data)
        return note_record.show_note_by_tag()

    @input_error
    def edit_note(self, data, notebook):
        new_note = input("Enter new note: ")
        note_record = notebook.find(data)
        return note_record.edit_tag_note(new_note)

    @input_error
    def delete_note(self, data, notebook):
        return notebook.delete_note_by_tag(data)

    @staticmethod
    def help():
        return help_message()

    @input_error
    def change_bot_color(self, data, color):
        if data == "blue":
            color.set_current_color(Fore.BLUE)
        elif data == "red":
            color.set_current_color(Fore.RED)
        elif data == "green":
            color.set_current_color(Fore.GREEN)
        elif data == "yellow":
            color.set_current_color(Fore.YELLOW)
        elif data == "cyan":
            color.set_current_color(Fore.CYAN)
        elif data == "magenta":
            color.set_current_color(Fore.MAGENTA)
        elif data == "white":
            color.set_current_color(Fore.WHITE)
        else:
            raise ValueError
        return f"Changing color to: {data}"
