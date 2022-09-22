#!/usr/bin/env python
"""
Simple command-line tools using sys.argv
"""
import sys

if __name__ == "__main__":
    print(f"The first argument: '{sys.argv[0]}'")  # The name of the script
    print(f"The second argument: '{sys.argv[1]}'")  # The first argument
    print(f"The third argument: '{sys.argv[2]}'")  # The second argument
    print(f"The fourth argument: '{sys.argv[3]}'")  # The third argument
