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


def main():
    contact_book = AddressBook()
    contact_book.load_data()

    while True:
        print("\n1. Add Contact")
        print("2. View Contact")
        print("3. Find Contact")
        print("4. Show All Contacts")
        print("5. Show Phone Numbers")
        print("6. Show Email")
        print("7. Show Address")
        print("8. Show Birthday")
        print("9. Upcoming Birthdays")
        print("10. Delete Contact")
        print("11. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11): ")

        if choice == '1':
            name = input("Enter name: ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            birthday = input("Enter birthday (DD.MM.YYYY): ")
            contact_book.add_contact(name, address, phone, email, birthday)
        elif choice == '2':
            name = input("Enter name to view contact: ")
            contact_book.view_contact(name)
        elif choice == '3':
            query = input("Enter search query: ")
            contact_book.find_contact(query)
        elif choice == '4':
            contact_book.show_all()
        elif choice == '5':
            name = input("Enter name to show phone numbers: ")
            contact_book.show_phone(name)
        elif choice == '6':
            name = input("Enter name to show email: ")
            contact_book.show_email(name)
        elif choice == '7':
            name = input("Enter name to show address: ")
            contact_book.show_address(name)
        elif choice == '8':
            name = input("Enter name to show birthday: ")
            contact_book.show_birthday(name)
        elif choice == '9':
            days = int(input("Enter the number of days for upcoming birthdays: "))
            upcoming = contact_book.upcoming_birthday(days)
            if upcoming:
                print(f"\nUpcoming Birthdays ({days} days or less):")
                for name, birthday in upcoming:
                    print(f"{name}: {birthday}")
            else:
                print("No upcoming birthdays.")
        elif choice == '10':
            days = int(input("Enter the number of days for upcoming birthdays: "))
            upcoming = contact_book.upcoming_birthdays(days)
            if upcoming:
                print(f"\nUpcoming Birthdays ({days} days or less):")
                for name, birthday in upcoming:
                    print(f"{name}: {birthday}")
            else:
                print("No upcoming birthdays.")
        elif choice == '11':
            contact_book.save_data()
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()