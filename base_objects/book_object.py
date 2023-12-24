from collections import UserDict, defaultdict
from datetime import datetime


class AddressBook(UserDict):
    def add_contact(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]

    def show_all(self):
        if self.data:
            print("\nAll Contacts:")
            return "\n".join(
                f"{name} - "
                f"Phone(s): {', '.join([phone.value for phone in value.phones])}, "
                f"E-mail(s): {', '.join([email.value for email in value.emails])}, "
                f"Address: {value.address}, "
                f"Birthday: {value.birthday}"
                for name, value in self.data.items())
        else:
            return "No contacts in the address book."

    def show_contact(self, name):
        if name in self.data:
            contact = self.data[name]
            return (f"\n{name}:\nPhone(s): {', '.join([phone.value for phone in contact.phones])}, "
                    f"E-mail(s): {', '.join([email.value for email in contact.emails if email != []])}, "
                    f"Address: {contact.address}, Birthday: {contact.birthday}")
        else:
            return f"Contact '{name}' not found."

    def show_phone(self, name):
        if name in self.data:
            contact = self.data[name]
            if contact.phones:
                return f"{name}'s phone(s): {', '.join([phone.value for phone in contact.phones])}"
            else:
                return f"{name} has no phone numbers."
        else:
            return f"Contact '{name}' not found."

    def show_email(self, name):
        if name in self.data:
            contact = self.data[name]
            if contact.emails:
                return f"{name}'s e-mail(s): {', '.join([email.value for email in contact.emails if email != []])}"
            else:
                return f"{name} has no email address."
        else:
            return f"Contact '{name}' not found."

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
        default_dict = defaultdict(list)
        today = datetime.today().date()

        for user in self.data:
            name = self.data[user].name.value
            birthday = self.data[user].birthday.value
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days
            if 0 <= delta_days < days:
                if birthday_this_year.strftime("%A") in ["Saturday", "Sunday"] and delta_days <= 5:
                    default_dict[birthday_this_year.strftime("Monday")].append(f"{name} {birthday}")
                else:
                    default_dict[birthday_this_year.strftime("%A")].append(f"{name} {birthday}")

        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        default_dict = {day: default_dict[day] for day in week}

        return default_dict

    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")
