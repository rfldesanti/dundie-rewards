import rich_click as click
import pkg_resources
from dundie import core
from rich.table import Table
from rich.console import Console



@click.group()
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """Dunde Mifflin Rewards System

    This CLI application controls DM rewards.
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database

    ## Features

    - Validates data
    - Parses the file
    - Loads to database
    """
    table = Table(title="Dunder Mifflin Associates")
    headers = ["name", "dept", "role", "created", "e-mail"]
    for header in headers:
        table.add_column(header, style="magenta")

    result = core.load(filepath)
    for person in result:
        table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)
