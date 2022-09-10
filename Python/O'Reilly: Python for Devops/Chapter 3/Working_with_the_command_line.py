import sys
import os
import subprocess

"""
It is better to be in a virtual environment when downloading special packages, so you don't mess up certain dependencies,
especially on linux where sometimes having too many dependencies is a cause of frustration and new installation of the entire system : ^).
In order to do that type:
    $python -m venv venv      //This creates a virtual environment with the name venv
    $source venv/bin/activate //This activates the virtual environment
Please for the love of god don't commit this folder to GitHub
"""

"""
Python offers tools for interacting with systems and shells. 
One of these tools is the sys modules, which offers access to variables and methods closely tied to the Python interpreter.
"""


def sys_module():
    """
    There are two dominant ways to interpret bytes during reading. The first, little endian, interprets each subsequent byte as having higher
    significance than the previous one. The second, big endian, assumes the first byte has the greatest significance and move down from there.
    """
    print(sys.byteorder)  # Prints the byte order of the system

    print(
        sys.getsizeof(1)
    )  # Returns the size of an object in bytes. This is useful when dealing with limited amounts of memory.

    print(
        sys.getrecursionlimit()
    )  # Returns the maximum depth of the Python interpreter's stack.

    print(sys.platform)  # Returns the platform on which the interpreter is running.

    """
    A more common situation is that you want to use a language feature or module that is only available in specific versions of Python. You can use 
    the sys.version_info to control behaviour based on the version of Python you are running. Here we print different messages for python 3.7,
    a Python version 3 that is below 3.7, and Python versions lower than 3.
    """
    if sys.version_info.major < 3:
        print("You are running an old version of Python and should upgrade")
    elif sys.version_info.minor < 7:
        print("You are not running the latest version of Python")
    else:
        print(
            f"You are running Python {sys.version_info.major}.{sys.version_info.minor} and all is well ^_^"
        )
