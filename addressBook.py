from datetime import datetime
import json

class AddressBook:
    def __init__(self):
        self.contacts = {}
        self.file_path = "address_book.json"

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                for name, contact_data in data.items():
                    contact = Record(name)
                    contact.add_address(contact_data['address'])
                    contact.add_phone(contact_data['phone'])
                    contact.add_email(contact_data['email'])
                    contact.add_birthday(contact_data['birthday'])
                    self.contacts[name] = contact
        except FileNotFoundError:
            pass 
    
    def save_data(self):
        with open(self.file_path, 'w') as file:
            data = {name: {
                'address': str(contact.address),
                'phone': [str(phone) for phone in contact.phones],
                'email': str(contact.email),
                'birthday': str(contact.birthday)
            } for name, contact in self.contacts.items()}
            json.dump(data, file, indent=2)

    def add_contact(self, name, address, phone, email, birthday):
        contact = Record(name)
        contact.add_address(address)
        contact.add_phone(phone)
        contact.add_email(email)
        contact.add_birthday(birthday)
        self.contacts[name] = contact

    def view_contact(self, name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print(f"Contact '{name}' not found.")

    def find_contact(self, query):
        matches = [name for name in self.contacts if re.search(query, name, re.IGNORECASE)]
        if matches:
            print(f"\nMatching contacts for '{query}':")
            for match in matches:
                print(self.contacts[match])
        else:
            print(f"No contacts found for '{query}'.")

    def show_all(self):
        if self.contacts:
            print("\nAll Contacts:")
            for name, contact in self.contacts.items():
                print(f"\n{name}:\n{contact}")
        else:
            print("No contacts in the address book.")

    def show_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"\n{name}:\n{contact}")
        else:
            print(f"Contact '{name}' not found.")

    def show_phone(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            if contact.phones:
                print(f"\n{name}'s Phone Numbers:")
                for phone in contact.phones:
                    print(phone)
            else:
                print(f"{name} has no phone numbers.")
        else:
            print(f"Contact '{name}' not found.")

    def show_email(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            if contact.email:
                print(f"\n{name}'s Email:")
                print(contact.email)
            else:
                print(f"{name} has no email address.")
        else:
            print(f"Contact '{name}' not found.")

    def show_address(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            if contact.address:
                print(f"\n{name}'s Address:")
                print(contact.address)
            else:
                print(f"{name} has no address.")
        else:
            print(f"Contact '{name}' not found.")

    def show_birthday(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
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

        for name, contact in self.contacts.items():
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
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def upcoming_birthdays(self, days):
        today = datetime.now()
        upcoming_birthdays = []

        for name, contact in self.contacts.items():
            birthday = contact.birthday.date
            next_birthday = datetime(today.year, birthday.month, birthday.day)

            if next_birthday < today:
                next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

            days_until_birthday = (next_birthday - today).days

            if 0 < days_until_birthday <= days:
                upcoming_birthdays.append((name, contact.birthday))

        return upcoming_birthdays