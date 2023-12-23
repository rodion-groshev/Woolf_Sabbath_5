from collections import UserList
from base_objects.contact_object import Note
from utilities import storage
from utilities.error_handler import NoteNotFound, input_error


from collections import UserList


class Notes(UserList):
    
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text
    
    
    def add_record(self, note):
        self.data.append(note)

    def remove_record(self, note_id):
        if 0 <= note_id < len(self.data):
            return self.data.pop(note_id)
        else:
            raise IndexError(f"Note with id {note_id} not found.")

    def edit_record(self, note_id, new_value):
        if 0 <= note_id < len(self.data):
            self.data[note_id] = new_value
        else:
            raise IndexError(f"Note with id {note_id} not found.")

    def search_records(self, query):
        matching_records = {}
        for index, record in enumerate(self.data):
            if query in record.value:
                matching_records[index] = record
        return matching_records

    def print_all_notes(self):
        return "\n".join([f"{index}. {record}" for index, record in enumerate(self.data)])
