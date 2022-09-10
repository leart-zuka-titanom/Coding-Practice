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


def sys_module_examples():
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

def os_module_examples():
        """
        You have seen the os module used in Chapter 2 for dealing with the filesystem. It also has a grab bag of various attributes and functions
        related to dealing with the operating system. Here are some examples.
        """
        print(os.getcwd()) # Returns the current working directory

        os.chdir('/tmp') # Changes the current working directory to /tmp
        print(os.getcwd())

        print(os.environ.get('LOGLEVEL')) # Returns the value of the LOGLEVEL environment variable

        os.environ['LOGLEVEL'] = 'DEBUG' # Sets the LOGLEVEL environment variable to DEBUG

        print(os.environ.get('LOGLEVEL'))

        print(os.getlogin()) # Returns the name of the user logged in

"""
The most common usage of the os module is to get settings from environment variables. These could be the level to set your logging, or secrets
such as API keys.
"""

"""
There are many instances when you need to run applications outside of Python from within your Python code. This could be built-in shell commands,
Bash scripts, or any other command-line application. To do this, you spawn a new process (instance of the application). The subprocess module
is the right choice when you want to spawn a process and run command within it. With subprocess, you can run your favorite shell commands or other
command-line software and collect its output from within Python. For the majority of use cases, you should use the subprocess.run function to spawn
processes.
"""

def subprocess_module_examples():
    cp = subprocess.run(['ls', '-l'], capture_output=True, universal_newlines=True)
    print(cp.stdout)
    """
    subprocess.run returns a CompletedProcess instance once the process completes. In this case we run the shell command ls with the argument -l to 
    see the contents of the current directory. We set it to capture stdout and stderr with the capture_output parameter. We then access the results
    using cp.stdout. If we run ls ls on a nonexistent directory, we get an error message in cp.stderr. 
    """
    cp = subprocess.run(['ls', '-l', '/nonexistent'], capture_output=True, universal_newlines=True)
    print(cp.stderr)
    """
    A better ways to handle errors is by using the check parameter. This raises an exception if the subprocess reports an error
    """
    cp = subprocess.run(['ls', '-l', '/nonexistent'], capture_output=True, universal_newlines=True, check=True)
    print(cp.stdout)

"""
A sort of problem with Python script is the fact that it runs the written code from top to bottom which is sometimes not ideal. This can be a problem
if you import a Python script into another one.
"""
def say_it():
    greeting = "Hello"
    target = "World"
    message = f"{greeting}, {target}!"
    print(message)

#say_it() # This function run whenever the script runs on the command line and also when the file is imported

"""
This should only be done with the most straightforward scripts, however. As already said, if this module is import into another one, it will execute
the code just as if it was run on the command line. Someone who is importing your module usually wants control over when its contents are invoked.
You can add functionality that only happens when called from the command line by using the global name variable. If the module is called directly on 
the command line, this sets it to the string main. The convention for modules running on the command line is to end with a block testing for this and
run command-line specific code from this block. To modify the script to run a function automatically only when invoked on the command line, but not 
during import, put the function invocation into the block after the test 
"""

if __name__ == '__main__':
    say_it()

"""
When you import this function, this block does not run, as the __name__ variable reflects the module path as imported. It runs when the module is run
directly.

The first step in creating command-line tools is separating code that should only run when invoked on the command line. The next step is to accept 
command-line arguments. Unless your tool only does one thing, you need to accept commands to know what to do. Also, command-line tools that do more
than the simplest tasks accept optional flags to configure their workings. Providing documentation is an very good practice.
"""