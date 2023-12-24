# Woolf_Sabbath_5

Personal assistant application allows you to store, manage and search your contacts. Your data is stored on disk to not lose any important information.

It allows you to:
  - Save contacts in the contact Book with:
    - Name
    - Address
    - Phone Number
    - E-Mail
    - BithDate
  - Show all contacts and details for them
  - Verifies the correctness of entered data
  - Find needed information
  - Edit all needed details

## Installation

The application is written in Python language and requires Python version 3 or greater.

The application also requires the following libraries to be installed:
```sh
pip install prompt-toolkit
pip install rich
```

Get application sources:
```sh
git clone git@github.com:rodion-groshev/Woolf_Sabbath_5.git
```

Go into the directorz and run it:
```sh
cd Woolf_Sabbath_5
python main.py
```

## Quick start

here couple of commands, that show how to add, search and delete.


    Welcome to the assistant bot!

    Enter the command: add-contact

    Enter the Name: John Doe
    Enter the phone: +38012345678
    Enter email: test@example.com          
    Enter the address: Some str. 25
    Enter a birthday: 01.01.2023
    Contact  added successfully.

    Enter the command: show-all

    All Contacts:
    - Phone(s): +38012345678, E-mail(s): test@example.com, Address: Spome str. 25, Birthday: 01.01.2023
    
    Enter the command: delete-contact John Doe
    Contact 'John Doe' deleted successfully.

    Enter the command: exit
    Good bye!

[Manual for all available commands](MANUAL.md)