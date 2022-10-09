#!/usr/bin/env python

"""
Command-line tool using argparse
"""
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Echo your input"
    )  # Create the parser object, with its documentation message.
    parser.add_argument("message", help="Message to echo")
    parser.add_argument(
        "--twice", "-t", help="Do it twice", action="store_true"
    )  # Store the optional argument as a boolean value.
    args = parser.parse_args()  # Parse the arguments

    print(args.message)
    if args.twice:
        print(args.message)

"""
The nice thing about argparse is that is automatically sets up help and usage messages based on the help and description text you supply.
"""
