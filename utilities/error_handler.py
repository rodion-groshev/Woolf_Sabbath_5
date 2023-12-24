
# Definining Exception for validators

class KeyExistInContacts(Exception):
    """Contacts exception from the validator"""
    pass


class KeyNotExistInContacts(Exception):
    """Invalid contact exception from the validator"""
    pass


class BadPhoneNumber(Exception):
    """Incorrect Phone exception from the validator"""
    pass


class PhoneNumberIsMissing(Exception):
    """Phone missing exception from the validator"""
    pass


class BadBirthdayFormat(Exception):
    """Incorrect Birthday exception from the validator"""
    pass


class BadEmailFormat(Exception):
    """Incorrect E-Mail exception from the validator"""
    pass


class NoteExists(Exception):
    """Note already exist exception from the validator"""
    pass


class NoteNotFound(Exception):
    """Incorrect Note ID exception from the validator"""
    pass


class NoteOperationError(Exception):
    """Incorrect Note operation exception from the validator"""
    pass


class ValidationException(Exception):
    """Validator failed with message exception to notify user"""
    def __init__(self, message):
        self.message = message


def input_error(func):
    """Input decorator to catch user error inputs from the validators"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Format is incorrect. Use help to find correct format."
        except KeyExistInContacts as e:
            return f"This contact exists {e}."
        except KeyNotExistInContacts as e:
            return f"This contact does not exist {e}. You should add it."
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
        except NoteExists as e:
            return f"Note already exists {e}."
        except NoteNotFound as e:
            return f"Note not found {e}."
        except NoteOperationError as e:
            return f"Note operation error {e}."

    return inner
