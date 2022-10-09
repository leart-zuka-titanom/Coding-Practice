#!/usr/bin/env python
"""
Command-line tool using click
"""
import click


@click.group()  # Create a top-level group under which other groups and commands will reside.
def cli():  # Create a function to act as teh top-level group. The click.group method transforms the function into a group.
    pass


@click.group(help="Ship related commands")  # Create a group to hold the ships commands.
def ships():
    pass


cli.add_command(
    ships
)  # Add the ships group as a command to the top-level group. Note that teh cli function is now a group with an add_command method.


@ships.command(
    help="Sail a ship"
)  # Add a command to the ships group. Notice that ships.command is used instead of click.command.
def sail():
    ship_name = "Your ship"
    print(f"{ship_name} is setting sail")


@ships.command(help="List all of the ships")
def list_ships():
    ships = ["John B", "Yankee Clipper", "Pequod"]
    print(f'Ships: {", ".join(ships)}')


@cli.command(help="Talk to a sailor")
@click.option("--greeting", default="Ahoy there", help="Greeting for sailor")
@click.argument("name")
def sailors(greeting, name):
    message = f"{greeting} {name}"
    print(message)


if __name__ == "__main__":
    cli()

"""
In comparison the click approach requires certainly less code than the argparse approach.
The user interface code is interspersed throughout the whole program; it is especially important when creating functions that solely act as groups.
If you have a complex program, with a complex interface, you should try as best as possible to isolate different functionalities.
By doing so, you make individual pieces easier to test and debug. In such case, you might choose argparse to keep your interface code separate.
"""
