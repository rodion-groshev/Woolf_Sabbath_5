import pickle
from base_objects.book_object import AddressBook
from base_objects.note_object import NoteBook


class Storage:
    """
    Storage class to persist contact and notes on disk

    Attributes
    ----------
    _filename : str
        filename to store data. Constant, can't be change.

    Methods
    -------
    save_to_disk(self, records_dict)
        Serialize and store objects
    read_from_disk_contacts(self)
        Read and de-serialize contacts
    def read_from_disk_notes(self):
        Read and de-serialize notes
    """

    def __init__(self, filename):
        self._filename = f"{filename}.pkl"

    def save_to_disk(self, records_dict):
        """
        Parameters
        ----------
        records_dict : dict
            dictionary of Record objects
        """

        try:
            with open(self._filename, "wb") as file:
                pickle.dump(records_dict, file)
        except Exception as e:
            pass

    def read_from_disk_contacts(self):
        """
        Returns
        -------
            dict
                AddressBook dictionary or empty dict
        """

        try:
            with open(self._filename, "rb") as file:
                loaded_records = pickle.load(file)
            return loaded_records
        except FileNotFoundError:
            # FIXME: function returns different types (should be dict)
            return AddressBook()
        except Exception as e:
            return {}

    def read_from_disk_notes(self):
        """
        Returns
        -------
            dict
                NoteBook dictionary or empty dict
        """

        try:
            with open(self._filename, "rb") as file:
                loaded_records = pickle.load(file)
            return loaded_records
        except FileNotFoundError:
            # FIXME: function returns different types (should be dict)
            return NoteBook()
        except Exception as e:
            return {}
