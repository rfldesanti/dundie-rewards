import argparse
from dundie.core import load

def main():
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