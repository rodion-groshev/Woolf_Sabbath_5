from collections import UserDict


class NoteBook(UserDict):
    """
    NoteBook represent Note in Record.

    This class defines all supported fields for the Note, 
    ways to manage them.

    Objects are stored in Records.

    Attributes
    ----------
    data : dict
        tags and Notes for them

    Methods
    -------
    add_note(self, note_record)
        Add new Note with specific Tag
    find(self, tag)
        Find Note by Tag
    show_all_notes
        Get all notes as a string
    """

    def add_note(self, note_record):
        """
        Parameters
        ----------
        note_record : Note
            Note object
        """
        self.data[note_record.tag.value] = note_record

    def find(self, tag):
        """
        Parameters
        ----------
        tag : Tag
            Tag object
        """
        return self.data[tag]

    def show_all_notes(self):
        """
        Returns
        -------
        string
            list of tags and Notes for themß
        """

        if self.data:
            print("\nAll Notes:")
            return "\n".join(
                f"{tag} - "
                f"Note: {record_note.note_memory.value}"
                for tag, record_note in self.data.items())
        else:
            return "No tag in the notebook book."
