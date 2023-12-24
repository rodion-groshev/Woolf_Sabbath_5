from rich.console import Console
from rich.table import Table
from rich import box


def birthday_output(upcoming_birthdays):
    console = Console()
    if upcoming_birthdays:
        table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE_HEAVY)
        table.add_column("Day", style="cyan", justify="center")
        table.add_column("Contacts", style="green", justify="center")

        for day, birthdays in upcoming_birthdays.items():
            table.add_row(day, ', '.join(birthdays))

        console.print(table)
    else:
        console.print("No upcoming birthdays.")
