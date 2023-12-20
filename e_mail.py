# class Email
import re

class Email:
    def __init__(self, email_address):
        if not email_address:
            self.email_address = None
        elif self.validate_email(email_address):
            self.email_address = email_address
        else:
            raise ValueError("Invalid email format.")

    @staticmethod
    def validate_email(email_address):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email_address) is not None
