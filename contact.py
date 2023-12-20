# Importing Classes
from name import Name
from phone import Phone
from e_mail import Email
from address import Address

class Contact:
    def __init__(self, first_name, last_name, phone_number=None, email_address=None, address=None):
        self.name = Name(first_name, last_name)
        self.phone = Phone(phone_number) if phone_number else None
        self.email = Email(email_address) if email_address else None
        self.address = Address(address) if address else None

    def __str__(self):
        return f"Name: {self.name.first_name} {self.name.last_name}, " \
               f"Phone: {self.phone.phone_number if self.phone else 'None'}, " \
               f"Email: {self.email.email_address if self.email else 'None'}, " \
               f"Adress: {self.address.address if self.address else 'None'}"
