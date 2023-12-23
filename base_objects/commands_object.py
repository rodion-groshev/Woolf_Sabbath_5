from base_objects.contact_object import Note
from utilities import storage
from utilities.error_handler import input_error
from base_objects.record_object import Record
from base_objects.note_object import Notes

class Commands:
    
    def __init__(self, book, notes):
        self.book = book
        self.notes = notes         
        
          
    @input_error
    def add_contact(self, book,):
        name = input("Enter the name: ")
        phone = input("Enter the phone: ")
        email = input("Enter email: ")
        address = input("Enter the address: ")
        birthday = input("Enter a birthday: ")

        record = Record(name)
        if phone:
            record.add_phone(phone)
        if email:
            record.add_email(email)
        if address:
            record.add_address(address)
        if birthday:
            record.add_birthday(birthday)
            
        book.add_contact(record)
        return f"Contact {name} added successfully."
    
    @input_error
    def add_note_contact(self, note_text):
        note_name = input("Enter the note naming: ")
        note_text = input("Enter the note text body: ")
        record = Record(note_name)
        if note_text:
            record.add_note(note_text)
        self.notes.add_record(record)
        return f"Contact {note_name} added successfully."

    
    @input_error
    def add_phone(self, args, book):
        name, phone = args
        record = book.find(name)
        record.add_phone(phone)
        return f"Phone: {phone} added to contact {name}."

    @input_error
    def add_email(self, args, book):
        name, email = args
        record = book.find(name)
        record.add_email(email)
        return f"Email: {email} added to contact {name}."

    @input_error
    def add_address(self, args, book):
        name, address = args
        record = book.find(name)
        record.add_address(address)
        return f"Address: {address} added to contact {name}."

    @input_error
    def add_birthday(self, args, book):
        name, birthday = args
        record = book.find(name)
        record.add_birthday(birthday)
        return f"Birthday: {birthday} added to contact {name}."

    @input_error
    def edit_phone(self, args, book):
        name, old_phone, new_phone = args
        if name in book:
            record = book.find(name)
            record.edit_phone(old_phone, new_phone)
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def edit_email(self, args, book):
        name, old_email, new_email = args
        if name in book:
            record = book.find(name)
            record.edit_email(old_email, new_email)
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def edit_address(self, args, book):
        name, address = args
        if name in book:
            record = book.find(name)
            record.edit_address(address)
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def edit_birthday(self, args, book):
        name, birthday = args
        if name in book:
            record = book.find(name)
            record.edit_birthday(birthday)
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def show_all(self, book):
        return book.show_all()

    @input_error
    def show_contact(self, args, book):
        name = args[0]
        return book.show_contact(name)

    @input_error
    def show_phone(self, args, book):
        name = args[0]
        return book.show_phone(name)

    @input_error
    def show_email(self, args, book):
        name = args[0]
        return book.show_email(name)

    @input_error
    def show_address(self, args, book):
        name = args[0]
        return book.show_address(name)

    @input_error
    def show_birthday(self, args, book):
        name = args[0]
        return book.show_birthday(name)

    @input_error
    def delete_contact(self, args, book):
        name = args[0]
        return book.delete_contact(name)

    @input_error
    def delete_phone(self, args, book):
        name, phone = args
        record = book.find(name)
        return record.delete_phone(phone)

    @input_error
    def delete_email(self, args, book):
        name, email = args
        record = book.find(name)
        return record.delete_email(email)

    @input_error
    def delete_address(self, args, book):
        name, address = args
        record = book.find(name)
        return record.delete_email(address)

    @input_error
    def delete_birthday(self, args, book):
        name, birthday = args
        record = book.find(name)
        return record.delete_email(birthday)
    
    
    
    
    
    @input_error
    def add_note(self, args):
        if args and len(args) > 0:
            note_text = args[0]
            self.note.add_record(Note(note_text))
            return f"Нотатку '{note_text}' додано успішно."
        else:
            return "Будь ласка, введіть текст для нотатки."


    def del_note(self, args):
        note_id = int(args[0]) 
        try:
            self.note.remove_record(note_id)
            return f"Note id {note_id} was removed."
        except IndexError:
            return f"Note with id {note_id} not found."

    def edit_note(self, args):
        note_id = int(args[0])  
        try:
            note = self.note.data[note_id]
            if args[1]:
                note.value = args[1]  
            return f"Note id {note_id} updated."
        except IndexError:
            return f"Note with id {note_id} not found."

    def search_note_by_tag(self, args):
        if args[0]:  
            matching_records = self.note.search_by_tag(args[0])
            return "\n".join(
                [f"{index}. {record}" for index, record in matching_records.items()]
            )
        else:
            return "Please provide a tag for searching."

    def search_note_by_query(self, args):
        if args[0]:  
            matching_records = self.note.search_records(args[0])
            return "\n".join(
                [f"{index}. {record}" for index, record in matching_records.items()]
            )
        else:
            return "Please provide a query for searching."

    
    def read_notes_all(self): 
        return self.note.print_all_notes()

    
    def help(self):
        print("\nAvailable Commands:")
        print("--------------------")
        print("add-contact <name> <address> <phone> <email> <birthday>")
        print("add-phone <name> <phone>")
        print("add-email <name> <email>")
        print("add-address <name> <address>")
        print("add-birthday <name> <birthday>")
        print("edit-phone <name> <old_phone> <new_phone>")
        print("edit-email <name> <old_email> <new_email>")
        print("edit-address <name> <new_address>")
        print("edit-birthday <name> <new_birthday>")
        print("show-all")
        print("show-phone <name>")
        print("show-email <name>")
        print("show-address <name>")
        print("show-birthday <name>")
        print("delete-contact <name>")
        print("delete-phone <name> <phone>")
        print("delete-email <name> <email>")
        print("delete-address <name>")
        print("delete-birthday <name>")
        print("birthday")
        print("add-note <id> <note>")
        print("del-note <id>")
        print("edit-note <id>")
        print("search-note <id> ")
        print("read-notes-all")
        print("add-note <id> <note>")
        print("exit")
        print("help")
