from collections import UserDict, defaultdict
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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
                return f"\n{name}'s Address:\n{contact.address}"
            else:
                return f"{name} has no address."
        else:
            return f"Contact '{name}' not found."

    def show_birthday(self, name):
        if name in self.data:
            contact = self.data[name]
            if contact.birthday:
                return f"\n{name}'s Birthday:\n{contact.birthday}"
            else:
                return f"{name} has no birthday."
        else:
            return f"Contact '{name}' not found."

    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def birthday_func(self, days):
        default_dict = defaultdict(list)
        today = datetime.today().date()

        for user in self.data:
            name = self.data[user].name.value
            birthday = self.data[user].birthday.value
            birthday_this_year = birthday.replace(year=today.year)
            if birthday_this_year == today:
                asking = input(f"Today {name}'s birthday {birthday_this_year}. "
                               f"Do you want to send greeting to {name}? [Y/N]: ")
                if asking == "Y":
                    subject = "Happy Birthday"
                    body = "Happy Birthday! 🎉 Wishing you all the best, health, and happiness!"
                    if self.data[name].emails:
                        to_email = ", ".join(email.value for email in self.data[name].emails)
                        smtp_server = "smtp.gmail.com"
                        smtp_port = 587
                        smtp_username = "alreadyexist22@gmail.com"
                        smtp_password = "qzwd lmlm gibl glan"
                        self.send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password)
                    else:
                        return "You must add email to contact"

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

    def send_email(self, subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
        smtp_server = smtplib.SMTP(smtp_server, smtp_port)
        smtp_server.starttls()
        smtp_server.login(smtp_username, smtp_password)
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        smtp_server.sendmail(smtp_username, to_email, msg.as_string())
        smtp_server.quit()

