from datetime import datetime
from utilities.error_handler import BadPhoneNumber, PhoneNumberIsMissing, ValidationException, BadBirthdayFormat
from base_objects.main_objects import Name, Phone, Field, Birthday, Email, Address, Tag, Note


class Record:
    """
    Record class represent Contact record in a Book.

    This class defines all supported fields for contacts, 
    ways to manage them.

    Objects are stored on disk.

    Attributes
    ----------
    name : Name
        Name object that stores Name
    phones : list
        list of Phone objects
    email : list
        list of Email objects
    address : Field
        Field object that contain Address
    address : Field
        Field object that contain Address

    Methods
    -------
    add_phone(self, phone)
        Add and validate new phone
    add_email(self, email)
        Add and validate new email
    add_address(self, address)
        Add and validate new address
    add_birthday(self, birthday)
        Add and validate new Birthday
    edit_phone(self, old_phone, new_phone)
        Edit and validate existing phone
    edit_email(self, old_email, new_email)
        Edit and validate existing email
    edit_address(self, new_address)
        Edit and validate existing address
    edit_birthday(self, new_birthday)
        Edit and validate existing birthday
    delete_phone(self, phone)
        Delete phone
    delete_email(self, email)
        Delete email
    delete_address(self)
        Delete address
    delete_birthday(self)
        Delete phone
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.address = None
        self.birthday = None

    def add_phone(self, phone):
        """
        Parameters
        ----------
        phone : string
            phone string

        Raises
        ------
        BadPhoneNumber
            phone string is incorrect, doesn't pass validator
        """

        new_phone = Phone(phone)
        if not new_phone.validate_phone():
            raise BadPhoneNumber(phone)
        self.phones.append(new_phone)

    def add_email(self, email):
        """
        Parameters
        ----------
        email : string
            email string

        Raises
        ------
        ValidationException
            email string is incorrect, doesn't pass validator
        """

        new_email = Email(email)
        if new_email.validate_email():
            self.emails.append(new_email)
        else:
            raise ValidationException(new_email)

    def add_address(self, address):
        """
        Parameters
        ----------
        address : string
            address string
        """

        # FIXME: validation is different from other methods in a class
        self.address = Address(address)

    def add_birthday(self, birthday):
        """
        Parameters
        ----------
        birthday : string
            birthday string

        Raises
        ------
        BadBirthdayFormat
            birthday string is incorrect, doesn't pass validator
        """

        new_birthday = Birthday(birthday)
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
        except ValueError:
            raise BadBirthdayFormat(new_birthday)
        self.birthday = new_birthday

    def edit_phone(self, old_phone, new_phone):
        """
        Parameters
        ----------
        old_phone : string
            old phone string
        new_phone : string
            new phone string

        Raises
        ------
        PhoneNumberIsMissing
            there is no such old phone
        ValidationException
            new_phone is incorrect, doesn't pass validator
        """

        if old_phone in self.phones:
            new_phone_obj = Phone(new_phone)
            if new_phone_obj.validate_phone():
                index = self.phones.index(old_phone)
                self.phones[index] = new_phone_obj
            else:
                raise ValidationException(new_phone_obj)
        else:
            raise PhoneNumberIsMissing(new_phone_obj)

    def edit_email(self, old_email, new_email):
        """
        Parameters
        ----------
        old_email : string
            old email string
        new_email : string
            new email string

        Raises
        ------
        ValidationException
            there is no such old email or
            new_email is incorrect, doesn't pass validator
        """

        if old_email in self.emails:
            new_email_obj = Email(new_email)
            if new_email_obj.validate_email():
                index = self.emails.index(old_email)
                self.emails[index] = new_email_obj
            else:
                # FIXME: same exception for validator and no e-mailß
                raise ValidationException(new_email_obj)
        else:
            raise ValidationException(new_email_obj)

    def edit_address(self, new_address):
        """
        Parameters
        ----------
        new_address : string
            new address string
        """

        self.address = Field(new_address)

    def edit_birthday(self, new_birthday):
        """
        Parameters
        ----------
        new_birthday : string
            new birthday

        Raises
        ------
        BadBirthdayFormat
            new birthday is incorrect, doesn't pass validator
        """

        try:
            datetime.strptime(new_birthday, "%d.%m.%Y")
        except ValueError:
            raise BadBirthdayFormat(new_birthday)
        self.birthday = new_birthday

    def delete_phone(self, phone):
        """
        Parameters
        ----------
        phone : string
            phone to delete

        Raises
        ------
        PhoneNumberIsMissing
            no such phone found
        """

        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise PhoneNumberIsMissing(phone)

    def delete_email(self, email):
        """
        Parameters
        ----------
        email : string
            email to delete

        Raises
        ------
        ValidationException
            no such email found
        """

        if email in self.emails:
            self.emails.remove(email)
        else:
            # FIXME: general exception
            raise ValidationException(email)

    def delete_address(self):
        self.address = None

    def delete_birthday(self):
        self.address = None

    def __str__(self):
        """Defaul implementation to represent class as string"""

        phones_str = ', '.join(str(phone) for phone in self.phones)
        emails_str = ', '.join(str(email) for email in self.emails)
        return (f"Record(name: {self.name}, phones: [{phones_str}], emails: [{emails_str}], address: {self.address}, "
                f"birthday: {self.birthday})")


class NoteRecord:
    """
    NoteRecord represent Note record in a Book.

    This class used to store Note Objects on disk.

    Attributes
    ----------
    tag : Tag
        Tag object that represents tag
    note_memory : Note
        Note object that represent note
    
    Methods
    -------
    add_note_record(self, note)
        Add new Note to the record
    edit_note(self, new_note)
        Replace current note with new one
    delete_note(self)
        Delete Note
    """

    def __init__(self, tag):
        """Init default fields"""

        self.tag = Tag(tag)
        self.note_memory = None

    def add_note_record(self, note):
        """
        Parameters
        ----------
        note : string
            note to add
        """

        self.note_memory = Note(note)

    def edit_tag_note(self, new_note):
        self.note_memory = Note(new_note)
        return f"Note by tag '{self.tag}' edited.\n"

    def show_note_by_tag(self):
        return f"Note by tag {self.tag}: {self.note_memory}"

    def delete_note(self):
        self.note_memory = None
