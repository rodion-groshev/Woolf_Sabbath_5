# Woolf-Sabbath_5

Personal assistant application allows you to store, manage and search your contacts. Your data is stored on disk to not lose any important information.

It allows you to:
  - Save contacts in the AddressBook with:
    - Name
    - Address
    - Phone Number
    - E-Mail
    - Birthday
  - Save notes in the NoteBook with:
    - Tag
    - Note
  - Show all contacts and details for them
  - Verifies the correctness of entered data
  - Find needed information
  - Edit all needed details
  - Send congratulations by email
  - Change color of the text

## Installation

The application is written in Python language and requires Python version 3 or greater.

You can install the application via pip to your local machine (for Mac use pip3 command):
```sh
pip install woolf-sabbat-5 *(check newest version)
```

The application also requires the following libraries to be installed:
```sh
pip install prompt-toolkit
pip install rich
pip install colorama
```

Get application sources:
```sh
git clone git@github.com:rodion-groshev/Woolf_Sabbath_5.git
```

Run the main Python script anywhere in the console (two options)::
```sh
python -m woolf-sabbat-5.main
# or you can write the following command anywhere in the console:
woolf-sabbat-5.main
```

## Quick start

Here a couple of commands, that show how to add, search and delete.


    Welcome to the assistant bot!

    Enter the command: add-contact John (or John Smith)

    Enter the phone: +380677777777
    Enter email: test@example.com          
    Enter the address: Some str. 25
    Enter a birthday: 01.01.2023
    Contact  added successfully.

    Enter the command: show-all

    All Contacts:
    John Smith - Phone(s): +380677777777, E-mail(s): example@mail.com, 
    Address: Main street 5, Birthday: 2000-01-01

    Enter the command: delete-contact John (or John Smith)
    Contact 'John Smith' deleted successfully.

    Enter the command: exit
    Good bye!