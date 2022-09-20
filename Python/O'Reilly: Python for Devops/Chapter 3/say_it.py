#!/usr/bin/env python

"""
To eliminate the need to explicitly call type python on the command line when you run your script, you can add the line '#!/usr/bin/env python' to the
top of your file. It tells the operating system to run the script with the Python interpreter. This is called a shebang line.
"""


def say_it():
    greeting = "Hello"
    target = "World"
    message = f"{greeting}, {target}!"
    print(message)


if __name__ == "__main__":
    say_it()

"""
Then make the file executable and call it in a shell without directly invoking Python.
So basically,
1. Add the shebang line to the top of the file
2. Make the file executable with the command 'chmod +x say_it.py'
3. Run the script with './say_it.py'
"""
