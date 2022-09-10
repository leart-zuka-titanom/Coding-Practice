#!/usr/bin/env python

"""
To eliminate the need to explicitly call type python on the command line when you run your script, you can add the line '#!/usr/bin/env python' to the
top of your file
"""

def say_it():
    greeting = "Hello"
    target = "World"
    message = f"{greeting}, {target}!"
    print(message)

if __name__ == '__main__':
    say_it()

"""
Then maek the file executable and call it in a shell without directly invoking Python
"""