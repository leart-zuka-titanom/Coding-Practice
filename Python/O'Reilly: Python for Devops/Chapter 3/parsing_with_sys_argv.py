#!/usr/bin/env python
"""
Simple command-line tool using sys.argv
"""
import sys


def say_it(greeting, target):
    message = f"{greeting}, {target}!"
    print(message)


if __name__ == "__main__":
    greeting = "Hello"
    target = "Joe"

    if "--help" in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"  # The help_message itself
        print(help_message)
        sys.exit()

    if "--name" in sys.argv:
        name_index = sys.argv.index("--name") + 1  # Get position after name flag
        if name_index < len(sys.argv):  # Check if there is a name after the flag
            target = sys.argv[name_index]  # Get the name

    if "--greeting" in sys.argv:
        greeting_index = (
            sys.argv.index("--greeting") + 1
        )  # Get position after greeting flag
        if greeting_index < len(
            sys.argv
        ):  # Check if there is a greeting after the flag
            greeting = sys.argv[greeting_index]  # Get the greeting

    say_it(greeting, target)

"""
This approach is fraught with complications and potential bugs.
If a user misspells or miscapitalizes a flag, the flag is ignored with no useful feedback.
If they use commands that are not supported or try to use more than one value with a flag, once again the error is ignored.
So don't use argv for production code unless specifically set out to write an argument parser.
"""
