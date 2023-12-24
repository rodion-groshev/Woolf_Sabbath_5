import re
from datetime import datetime
from base_objects.main_objects import Email
from utilities.error_handler import input_error, BadPhoneNumber, BadEmailFormat, BadBirthdayFormat
from base_objects.record_object import Record, NoteRecord
from utilities.help_message import help_message
from utilities.birtday_output import birthday_output


class Commands:
    """
    Command class implement different user commands,
    asking for additional parameters.

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
    add_contact(self, data, book)
        Add and validate new contact to the AddressBook
    add_phone(self, name, book)
        Add new phone for the specific name and AddressBook
    add_email(self, name, book)
        Add new email for the specific name and AddressBook
    add_address(self, name, book)
        Add new address for the specific name and AddressBook
    add_birthday(self, name, book)
        Add new birthday for the specific name and AddressBook
    edit_phone(self, name, book)
        Edit phone for the specific name and AddressBook
    edit_email(self, name, book)
        Edit email for the specific name and AddressBook
    edit_address(self, name, book)
        Edit address for the specific name and AddressBook
    edit_birthday(self, name, book)
        Edit birthday for the specific name and AddressBook
    show_all(self, book)
        Returns string with all contacts in AddressBook
    show_contact(self, name, book)
        Returns string with contact detail for specific name 
        from AddressBook
    show_phone(self, name, book)
        Returns phone string for specific name from AddressBook
    show_email(self, name, book)
        Returns email string for specific name from AddressBook
    show_address(self, name, book)
        Returns address string for specific name from AddressBook
    show_birthday(self, name, book)
        Returns birthday string for specific name from AddressBook
    delete_contact(self, name, book)
        Delete contact for specific name from AddressBook
    delete_phone(self, name, book)
        Delete phone for specific name from AddressBook
    delete_email(self, name, book)
        Delete email for specific name from AddressBook
    delete_address(self, name, book)
        Delete address for specific name from AddressBook
    delete_birthday(self, name, book)
        Delete birthday for specific name from AddressBook
    upcoming_birthday(self, days, book)
        Returns list of upcomming birthdays as string
        from AddressBook
    add_new_note(self, data, notebook)
        Add new Note for the specific name from NoteBook
    show_all_notes(self, notebook)
         Returns string with all Notes in NoteBook
    """

    @input_error
    def add_contact(self, data, book):
        """
        Function asks for user input for additional parameter.

        Parameters
        ----------
        data : string
            contact data
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """
        
        phone = input("Enter the phone: ")
        email = input("Enter email: ")
        address = input("Enter the address: ")
        birthday = input("Enter a birthday: ")
        record = Record(data)

        if phone:
            record.add_phone(phone)
        if email:
            record.add_email(email)
        if address:
            record.add_address(address)
        if birthday:
            record.add_birthday(birthday)
        book.add_contact(record)
        return f"Contact {data} added successfully."

    @input_error
    def add_phone(self, name, book):
        """
        Function asks for user input for additional parameter.
        
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """

        phone = input("Enter the phone number: ")
        record = book.find(name)
        record.add_phone(phone)
        return f"Phone: {phone} added to contact {name}."

    @input_error
    def add_email(self, name, book):
        """
        Function asks for user input for additional parameter.
        
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """

        email = input("Enter the email: ")
        record = book.find(name)
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if not re.match(email_pattern, email):
            raise BadEmailFormat(email)
        record.add_email(email)
        return f"Email: {email} added to contact {name}."

    @input_error
    def add_address(self, name, book):
        """
        Function asks for user input for additional parameter.
        
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """

        address = input("Enter the address: ")
        record = book.find(name)
        record.add_address(address)
        return f"Address: {address} added to contact {name}."

    @input_error
    def add_birthday(self, name, book):
        """
        Function asks for user input for additional parameter.
        
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """

        birthday = input("Enter the phone number: ")
        record = book.find(name)
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
        except ValueError:
            raise BadBirthdayFormat(birthday)
        record.add_birthday(birthday)
        return f"Birthday: {birthday} added to contact {name}."

    @input_error
    def edit_phone(self, name, book):
        """
        Function asks for user input for additional parameter.
        
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """

        old_phone = input("Enter the old phone number: ")
        new_phone = input("Enter the new phone number: ")
        if name in book:
            record = book.find(name)
            phone_pattern = re.compile(r'^\+38\d{9,10}$')
            if not re.match(phone_pattern, new_phone):
                raise BadPhoneNumber(new_phone)
            record.edit_phone(old_phone, new_phone)
            return f"Contact {name} updated."
        else:
            return "Contact not found"

    @input_error
    def edit_email(self, name, book):
        """
        Function asks for user input for additional parameter.
        
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """

        old_email = input("Enter the old email address: ")
        new_email = input("Enter the new email address: ")
        if name in book:
            record = book.find(name)
            email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if not re.match(email_pattern, new_email):
                raise BadEmailFormat(new_email)
            record.edit_email(Email(old_email), Email(new_email))
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def edit_address(self, name, book):
        """
        Function asks for user input for additional parameter.
        
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """

        address = input("Enter the address: ")
        if name in book:
            record = book.find(name)
            record.edit_address(address)
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def edit_birthday(self, name, book):
        """
        Function asks for user input for additional parameter.
        
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """

        birthday = input("Enter the birthday date: ")
        if name in book:
            record = book.find(name)
            try:
                datetime.strptime(birthday, "%d.%m.%Y")
            except ValueError:
                raise BadBirthdayFormat(birthday)
            record.edit_birthday(birthday)
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def show_all(self, book):
        """
        Parameters
        ----------
        book: dict
            AddressBook objects dictionary
        """

        return book.show_all()

    @input_error
    def show_contact(self, name, book):
        """
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        """

        return book.show_contact(name)

    @input_error
    def show_phone(self, name, book):
        """
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        """

        return book.show_phone(name)

    @input_error
    def show_email(self, name, book):
        """
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        """

        return book.show_email(name)

    @input_error
    def show_address(self, name, book):
        """
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        """

        return book.show_address(name)

    @input_error
    def show_birthday(self, name, book):
        """
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        """

        return book.show_birthday(name)

    @input_error
    def delete_contact(self, name, book):
        """
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        """

        return book.delete_contact(name)

    @input_error
    def delete_phone(self, name, book):
        """
        Function asks for user input for additional parameter.
        
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """

        phone = input("Enter the phone number: ")
        record = book.find(name)
        return record.delete_phone(phone)

    @input_error
    def delete_email(self, name, book):
        """
        Function asks for user input for additional parameter.
        
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        
        Returns
        -------
        string
            message to the user if command was succesfull or not
        """

        email = input("Enter the email: ")
        record = book.find(name)
        return record.delete_email(email)

    @input_error
    def delete_address(self, name, book):
        """
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        """

        record = book.find(name)
        return record.delete_address()

    @input_error
    def delete_birthday(self, name, book):
        """
        Parameters
        ----------
        name : string
            name for which to add new phone
        book: dict
            AddressBook objects dictionary
        """

        record = book.find(name)
        return record.delete_birthday()

    @input_error
    def upcoming_birthday(self, days, book):
        """
        Parameters
        ----------
        days : string
            date range
        book: dict
            AddressBook objects dictionary
        """

        birthday_output(book.upcoming_birthday(int(days)), book)

    @staticmethod
    def help():
        return help_message()

    def add_new_note(self, data, notebook):
        """
        Parameters
        ----------
        name : string
            name for which to add new phone
        notebook: dict
            NoteBook objects dictionary
        """

        tag = data
        note_input = input("Enter the note: ")
        note_record = NoteRecord(tag)
        note_record.add_note_record(note_input)
        notebook.add_note(note_record)
        return f"Note {tag} added successfully."

    def show_all_notes(self, notebook):
        """
        Parameters
        ----------
        name : string
            name for which to add new phone
        notebook: dict
            NoteBook objects dictionary
        """

        return notebook.show_all_notes()
