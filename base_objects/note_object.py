from collections import UserList
from base_objects.contact_object import Note
from utilities.error_handler import NoteNotFound, input_error
from utilities.storage import Storage




class Note(UserList):
    def __init__(self, storage: Storage):
        self.storage = storage
        data = storage.read_from_disk()
        self.data = data if isinstance(data, list) else list(data.values())
        print(self.print_all_notes())

    def add_record(self, rec: Note):
        if not isinstance(rec, Note):
            raise ValueError("Record must be an instance of NoteField")
        self.data.append(rec)

    def search_records(self, gets: str):
        matching_records = {}
        for index, record in enumerate(self.data):
            if gets in record.value:
                matching_records[index] = record
        return matching_records

    def edit_record(self, rec_id: int, new_value: Note):
        if 0 <= rec_id < len(self.data):
            self.data[rec_id] = new_value
        else:

            def throw_bad_note_index(id: int):
                raise NoteNotFound(f"Note index {id} out of range.")

            input_error(throw_bad_note_index)

    def remove_record(self, rec_id: int):
        if 0 <= int(rec_id) < len(self.data):
            return self.data.pop(int(rec_id))
        else:
            def throw_bad_note_index(id: int):
                raise NoteNotFound(f"Note index {id} out of range.")

            input_error(throw_bad_note_index, int(rec_id))

    def print_all_notes(self):
        return (
            "NOTES: \n"
            + "\n".join(
                [f"{index}. {record}" for index, record in enumerate(self.data)]
            )
            + "\n"
        )
