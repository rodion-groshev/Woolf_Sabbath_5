from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    def add_contact(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]

    def show_all(self):
        if self.data:
            print("\nAll Contacts:")
            for name, contact in self.data.items():
                print(f"\n{name}:\n{contact}")
        else:
            print("No contacts in the address book.")

    def show_contact(self, name):
        if name in self.data:
            contact = self.data[name]
            print(f"\n{name}:\n{contact}")
        else:
            print(f"Contact '{name}' not found.")

    def show_phone(self, name):
        if name in self.data:
            contact = self.data[name]
            if contact.phones:
                print(f"\n{name}'s Phone Numbers:")
                for phone in contact.phones:
                    print(phone)
            else:
                print(f"{name} has no phone numbers.")
        else:
            print(f"Contact '{name}' not found.")

    def show_email(self, name):
        if name in self.data:
            contact = self.data[name]
            if contact.email:
                print(f"\n{name}'s Email:")
                print(contact.email)
            else:
                print(f"{name} has no email address.")
        else:
            print(f"Contact '{name}' not found.")

    def show_address(self, name):
        if name in self.data:
            contact = self.data[name]
            if contact.address:
                print(f"\n{name}'s Address:")
                print(contact.address)
            else:
                print(f"{name} has no address.")
        else:
            print(f"Contact '{name}' not found.")

    def show_birthday(self, name):
        if name in self.data:
            contact = self.data[name]
            if contact.birthday:
                print(f"\n{name}'s Birthday:")
                print(contact.birthday)
            else:
                print(f"{name} has no birthday.")
        else:
            print(f"Contact '{name}' not found.")

    def upcoming_birthday(self, days):
        today = datetime.now()
        upcoming_birthdays = []

        for name, contact in self.data.items():
            if contact.birthday:
                birthday = contact.birthday.date
                next_birthday = datetime(today.year, birthday.month, birthday.day)

                if next_birthday < today:
                    next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

                days_until_birthday = (next_birthday - today).days

                if 0 < days_until_birthday <= days:
                    upcoming_birthdays.append((name, contact.birthday))

        return upcoming_birthdays

    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def upcoming_birthdays(self, days):
        today = datetime.now()
        upcoming_birthdays = []

        for name, contact in self.data.items():
            birthday = contact.birthday.date
            next_birthday = datetime(today.year, birthday.month, birthday.day)

            if next_birthday < today:
                next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

            days_until_birthday = (next_birthday - today).days

            if 0 < days_until_birthday <= days:
                upcoming_birthdays.append((name, contact.birthday))

        return upcoming_birthdays
