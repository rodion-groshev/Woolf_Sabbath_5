# class Adress
class Address:
    def __init__(self, address):
        if not address:
            raise ValueError("The address cannot be empty.")
    @staticmethod
    def validate_address(address):
        # Перевірка довжини адреси
        if len(address) < 5 or len(address) > 100:
            raise ValueError("Адреса повинна містити від 5 до 100 символів.")
        # Перевірка на недопустимі символи
        if any(char in address for char in "!@#$%^&*()"):
            raise ValueError("The address contains invalid characters.")
        return address.strip()
    