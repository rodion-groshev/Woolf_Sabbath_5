from rich.console import Console
from rich.table import Table


def help_message():
    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Available Commands", style="dim", width=50, justify="center")
    table.add_column("Info", style="dim", width=25, justify="center")

    table.add_row(
        "add-contact <name> <address> <phone> <email> <birthday>",
        "Add contact",
    )

    table.add_row("----------------------------------------------",
                  "-----------------------"
                  )

    table.add_row(
        "exit",
        "Close program"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "add-phone <name> <phone>",
        "Add phone to contact",
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "add-email <name> <email>",
        "Add email to contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "add-address <name> <address>",
        "Add address to contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "add-birthday <name> <birthday>",
        "Add birthday to contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "edit-phone <name> <old_phone> <new_phone>",
        "Change phone number in contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "edit-email <name> <old_email> <new_email>",
        "Add email to contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "edit-address <name> <new_address>",
        "Change address in contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "edit-birthday <name> <new_birthday>",
        "Change birthday in contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "show-all",
        "Display all contacts"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "show-phone <name>",
        "Display phone number by name"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "show-email <name>",
        "Display email by name"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "show-address <name>",
        "Display address by name"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "show-birthday <name>",
        "Display birthday by name"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "delete-contact <name>",
        "Delete contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "delete-phone <name> <phone>",
        "Delete phone in contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "delete-email <name> <email>",
        "Delete email in contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "delete-address <name>",
        "Delete address in contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "delete-birthday <name>",
        "Delete birthday in contact"
    )

    table.add_row("---------------------------------------------",
                  "----------------------"
                  )

    table.add_row(
        "help",
        "All possible commands"
    )

    console.print(table)
