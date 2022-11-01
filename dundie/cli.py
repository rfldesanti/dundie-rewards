<<<<<<< Updated upstream
import argparse
from dundie.core import load
=======
import rich_click as click
import pkg_resources
from dundie import core
from rich.table import Table
from rich.console import Console

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = True
click.rich_click.APPEND_METAVARS_HELP = True

>>>>>>> Stashed changes

@click.group()
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
<<<<<<< Updated upstream
    parser = argparse.ArgumentParser(
    description="Dunder Mifflin Rewards CLI",
    epilog="Enjoy and use with caution",       
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="subcommand to run",
        choices=("load", "show", "send")
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="filepath to load",
    )

    args = parser.parse_args()
    print(*globals()[args.subcommand](args.filepath))
=======
    """Dunde Mifflin Rewards System

    This application controls DM rewards.
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
>>>>>>> Stashed changes
