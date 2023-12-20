# Class Phone
import re
class Phone:
    def __init__(self, phone_number):
        if not phone_number:
            self.phone_number = None
        elif self.validate_phone(phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError("Invalid phone number format.")

    @staticmethod
    def validate_phone(phone_number):
        pattern = r"^\+?(\d{10,15})$"  # перевірка на довжину номера
        return re.match(pattern, phone_number) is not None
