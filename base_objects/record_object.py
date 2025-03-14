from datetime import datetime

from utilities.error_handler import (
    BadEmailFormat,
    BadPhoneNumber,
    EmailNotFound,
    PhoneNumberIsMissing,
    ValidationException,
    BadBirthdayFormat,
)
from base_objects.main_objects import (
    Name,
    Phone,
    Field,
    Birthday,
    Email,
    Address,
    Tag,
    Note,
)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.address = None
        self.birthday = None

    def add_phone_record(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def add_email_record(self, email):
        new_email = Email(email)
        self.emails.append(new_email)

    def add_address_record(self, address):
        self.address = Address(address)

    def add_birthday_record(self, birthday):
        new_birthday = Birthday(birthday)
        self.birthday = new_birthday

    def edit_phone_record(self, old_phone, new_phone):
        if old_phone in [str(phone_obj) for phone_obj in self.phones]:
            new_phone_obj = Phone(new_phone)
            self.phones = [
                phone_obj if str(phone_obj) != old_phone else new_phone_obj
                for phone_obj in self.phones
            ]
        else:
            raise PhoneNumberIsMissing(old_phone)

    def edit_email_record(self, old_email, new_email):
        if old_email in [str(email_obj) for email_obj in self.emails]:
            new_email_obj = Email(new_email)
            self.emails = [
                email_obj if str(email_obj) != old_email else new_email_obj
                for email_obj in self.emails
            ]
        else:
            raise ValidationException("Email address not found.")

    def edit_address_record(self, new_address):
        self.address = Address(new_address)

    def edit_birthday_record(self, new_birthday):
        new_birthday_obj = Birthday(new_birthday)
        self.birthday = new_birthday_obj

    def delete_phone_record(self, phone):
        if phone in [str(phone_obj) for phone_obj in self.phones]:
            self.phones = [
                phone_obj for phone_obj in self.phones if str(phone_obj) != phone
            ]
        else:
            raise PhoneNumberIsMissing(phone)

    def delete_email_record(self, email):
        if email in [str(email_obj) for email_obj in self.emails]:
            self.emails = [
                email_obj for email_obj in self.emails if str(email_obj) != email
            ]
        else:
            raise ValidationException(email)

    def delete_address_record(self):
        self.address = None

    def delete_birthday_record(self):
        self.birthday = None

    def __str__(self):
        phones_str = ", ".join(str(phone) for phone in self.phones)
        emails_str = ", ".join(str(email) for email in self.emails)
        return (
            f"Record(name: {self.name}, phones: [{phones_str}], emails: [{emails_str}], address: {self.address}, "
            f"birthday: {self.birthday})"
        )


class NoteRecord:
    def __init__(self, tag):
        self.tag = Tag(tag)
        self.note_memory = None

    def add_note_record(self, note):
        self.note_memory = Note(note)

    def edit_tag_note(self, new_note):
        self.note_memory = Note(new_note)
        return f"Note by tag '{self.tag}' edited.\n"

    def show_note_by_tag(self):
        return f"Note by tag {self.tag}: {self.note_memory}"

    def delete_note(self):
        self.note_memory = None
