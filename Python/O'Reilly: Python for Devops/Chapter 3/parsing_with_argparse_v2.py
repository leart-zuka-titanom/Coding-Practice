#!/usr/bin/env python

"""
Command-line tool using argparse
"""
import argparse


def sail():
    ship_name = "Your ship"
    print(f"{ship_name} is setting sail!")


def list_ships():
    ships = ["John B", "Yankee Clipper", "Pequod"]
    print(f"Ships: {', '.join(ships)}")


def greet(greeting, name):
    message = f"{greeting} {name}"
    print(message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Maritime control"
    )  # Create a top-level parser

    parser.add_argument("--twice", "-t", help="Do it twice", action="store_true")
    """
    Adds a top-level argument that can be used along with any command under this parser's hierarchy.
    """

    subparsers = parser.add_subparsers(dest="func")
    """
    Create a subparser object to hold the subparsers. The dest is the name of the attribute used to choose a subparser. 
    """

    ship_parser = subparsers.add_parser(
        "ships", help="Ship related commands"
    )  # Add a subparser for the ships command
    ship_parser.add_argument("command", choices=["list", "sail"])
    """
    Add a command to the ships subparser. The choices parameter gives a list of possible choices for the command.
    """

    sailor_parser = subparsers.add_parser("sailors", help="Talk to a sailor")
    sailor_parser.add_argument("name", help="Sailors name")
    sailor_parser.add_argument(
        "--greeting", "-g", help="Greeting", default="Ahoy there"
    )

    args = parser.parse_args()
    if (
        args.func == "sailors"
    ):  # Check which subparser is used by checking the func value.
        greet(args.greeting, args.name)
    elif args.command == "list":
        list_ships()
    else:
        sail()
