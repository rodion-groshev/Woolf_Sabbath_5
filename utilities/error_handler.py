class KeyExistInContacts(Exception):
    pass


class BadPhoneNumber(Exception):
    pass


class PhoneNumberIsMissing(Exception):
    pass


class BadBirthdayFormat(Exception):
    pass


class BadEmailFormat(Exception):
    pass


class EmailNotFound(Exception):
    pass


class NoteExists(Exception):
    pass


class NoteNotFound(Exception):
    pass


class NoteOperationError(Exception):
    pass


class ValidationException(Exception):
    pass


class EmptyFieldsException(Exception):
    pass


class EmptyNameFormat(Exception):
    pass


class EmptyPhonesStorage(Exception):
    pass


class EmptyAddressBook(Exception):
    pass


class EmptyEmailStorage(Exception):
    pass


class EmptyAddressStorage(Exception):
    pass


class EmptyBirthdayStorage(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Format is incorrect. Use help to find correct format."
        except KeyError as e:
            return f"This contact does not exist {e}. You should add it."
        except IndexError:
            return f"Bad arguments {args[1:]}."
        except BadPhoneNumber as e:
            return f"Phone format '{e}' is incorrect. It should be +380*********."
        except PhoneNumberIsMissing as e:
            return f"This number does not exist {e}. You should add it."
        except BadBirthdayFormat as e:
            return f"Birthday format '{e}' is incorrect. It should be DD.MM.YYYY."
        except BadEmailFormat as e:
            return f"Email format '{e}' is incorrect. It should be example@gmail.com. "
        except EmailNotFound as e:
            return f"Email not found {e}."
        except KeyExistInContacts as e:
            return f"This contact exists {e}."
        except NoteExists as e:
            return f"Note already exists {e}."
        except NoteNotFound as e:
            return f"Note not found {e}."
        except NoteOperationError as e:
            return f"Note operation error {e}."
        except EmptyFieldsException as e:
            return f"Enter at least one field. {e}"
        except ValidationException as e:
            return f"Enter at least one field. {e}"
        except EmptyNameFormat:
            return "Incorrect format. Format must be: <command> <name>"
        except EmptyPhonesStorage:
            return "No phones to display"
        except EmptyAddressBook:
            return "No contacts in the address book"
        except EmptyEmailStorage:
            return "No email addresses to display"
        except EmptyAddressStorage:
            return "No addresses to display"
        except EmptyBirthdayStorage:
            return "No birthday to display"

    return inner
