#!/usr/bin/env python
"""
Simple Click example
"""
import click


@click.command()
@click.option("--greeting", default="Hiya", help="How do you want to greet?")
@click.option("--name", default="Tammy", help="Who do you want to greet?")
def greet(greeting, name):
    print(f"{greeting}, {name}")


if __name__ == "__main__":
    greet()

"""
click.command indicates that a function should be exposed to command-line access.
click.option adds an argument to the command-line, automatically linking to the function parameter of the same name
(--greeting to greet and --name to name).
click does some work behind the scenes so that we can call our greet method in our main block without parameters that are covered by option decorators.
"""
