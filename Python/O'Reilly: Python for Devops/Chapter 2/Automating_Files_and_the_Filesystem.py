import pathlib
import json
from pprint import pprint
import csv
import pandas as pd
import hashlib
from cryptography.fernet import Fernet
import os
import fire

"""
It is better to be in a virtual environment when downloading special packages, so you don't mess up certain dependencies, 
especially on linux where sometimes having too many dependencies is a cause of frustration and new installation of the entire system : ^).
In order to do that type:
    $python -m venv venv      //This creates a virtual environment with the name venv
    $source venv/bin/activate //This activates the virtual environment
Please for the love of god don't commit this folder to GitHub
"""


def simple_read_1():
    """
    This is a simple way to open a file and read its contents
    """
    file_path = "LinAlg"  # This is the relative file path to the file you want to read
    open_file = open(
        file_path, "r"
    )  # This is the function that essentially opens the file. By default, the mode will be read, but you can also choose to write the file by
    # givin 'w' as the argument
    text = (
        open_file.read()
    )  # This reads the file as a whole. You also have the option to use .readlines() in order to read the file line by line, which will also have
    # an effect on how the file will be treated.
    print(len(text))
    print(open_file)
    open_file.close()  # It is always good to close the file since Python doesn't take care of that automatically


def simple_read_2():
    """
    This is another way to open a file and read its contents. In this case the with function is being used which makes it much cleaner tbh
    """
    file_path = "LinAlg"
    with open(file_path, "r") as open_file:
        text = open_file.read()
        print(text)


def simple_write():
    """
    This is a simple way to write a file
    """
    text = "Hi I'm learning how to write a file with Python \n"
    with open(
        "Message", "w"
    ) as opened_file:  # The open function creates a file if it does not already exist and overwrites if it does. If you want to simply append to
        # the file, use the append flag a
        opened_file.write(
            text
        )  # Basically the same as open. The \n in the message was added so that when you simply print the content of the file via cat the shell
        # prompt is being printed in the next line.


def file_handler_pathlib_read():
    path = pathlib.Path(
        "/home/leart/Learnding/Python/O'Reilly: Python for Devops/Chapter 2/Message"
    )  # Apparently you have to give the full path lul
    print(
        path.read_text()
    )  # In order to read binary data (e.g. from like an image for whatev reason) use path.read_bytes()


def file_handler_pathlib_write():
    path = pathlib.Path(
        "/home/leart/Learnding/Python/O'Reilly: Python for Devops/Chapter 2/Message"
    )  # Appareantly you have to give the full path lul
    path.write_text("I now know how to write files with the library pathlib \(^0^)/ \n")


def read_json_wrong():
    with open("action.json", "r") as opened_file:
        policy = (
            opened_file.readlines()
        )  # Basically this is the wrong way of reading files like jsons
        """Problem with files like .json files is that because of the way they're saved, 
        a simple readlines() will lead to the file not being displayed properly, 
        that's why we need some helper functions"""


def read_json_right():
    with open("action.json", "r") as opened_file:
        policy = json.load(opened_file)  # This is the correct way of reading jsons
        pprint(
            policy
        )  # The pprint module automatically formats Python objects for printing so that they're more readable n' stuff
        policy["Statement"][
            "Resource"
        ] = "S3"  # This is how you then use the data from the file to do whatever you please
        pprint(policy)
    with open("action.json", "w") as opened_file:
        json.dump(policy, opened_file)
        pprint(policy)


"""
The book now talks about some other languages used in configuration files like YAML or languages used in data serialization like XML.
I will not talk about them here since first I've never used them and second if I feel the need to learn them I will do so in the future.
(Call me lazy ion care)
"""


def read_csv():
    file_path = "opsd_germany_daily.csv"  # comma-seperated values (CSV) are basically just data stored in a table format and is common for
    # spreadsheet data.
    with open(file_path, newline="") as csv_file:
        off_reader = csv.reader(csv_file, delimiter=",")
        """
        The csv reader object iterates through the .csv file one line at a time, allowing you to process data one row at a time.
        """
        for _ in range(5):
            print(next(off_reader))


"""
Legggooo pandas.
The pandas package is a mainstay in the data science world and includes a data structure, the pandas.DataFrame, which acts like a data table.
The DataFrame allows you to do statistical analysis or manipulate by rows and columns if you have table-like data.
"""


def pandas_stuff():
    df = pd.read_csv(
        "opsd_germany_daily.csv"
    )  # This is how you read a csv file with pandas
    print(type(df))
    print(df.head(3))  # This is how you print the first 3 rows of the dataframe
    print(
        df.describe()
    )  # This is how you print some basic statistics about the dataframe
    print(df["Consumption"])  # This is how you print a specific column of the dataframe
    """
    the pandas package is an insanely powerful tool for data analysis and manipulation and anyone who performs basic data analysis,
     so me a physicist ._., should  really invest some itme into it.
    """


"""
The book now goes into detail on how to process large files. 
I will not talk about that here since if I feel the need to learn it I will do so in the future.
(Call me lazy ion care)
"""


def hashlib_encryption():
    secret = "This is the password or a document text"
    bsecret = secret.encode()  # This is how you encode a string into bytes
    m = hashlib.md5()  # This is how you create a hash object
    m.update(bsecret)  # This is how you update the hash object with the bytes
    print(m.digest())  # This is how you digest the hash object


def cryptography_encryption():
    key = Fernet.generate_key()  # This is how you generate a key
    print(key)
    f = Fernet(key)  # This is how you create a Fernet object
    message = b"Secrets go here"
    encrypted = f.encrypt(message)  # This is how you encrypt a message
    print(encrypted)
    decrypted = f.decrypt(encrypted)  # This is how you decrypt a message
    print(decrypted)


"""
The book now talks about the os module and its wide variety of functions.
The os module handles many low-level operating system calls and attempts to offer a consistent interface across multiple operating systems.
"""


def os_basic_functions():
    print(os.listdir("."))  # This is how you list the contents of a directory
    os.rename("Message2", "Message")  # This is how you rename a file
    #   os.chmod("my_script.py", 0o777) # This is how you change the permissions of a file
    os.mkdir("new_dir")  # This is how you create a directory
    os.makedirs(
        "new_dir/new_dir2"
    )  # This is how you create a directory and all its parents
    os.remove("file")  # This is how you remove a file
    os.rmdir("new_dir")  # This is how you remove a directory
    os.removedirs(
        "new_dir/new_dir2"
    )  # This is how you remove a directory and all its parents
    print(os.stat("Message"))  # This is how you get the status of a file


def os_dir_file_functions():
    cur_dir = os.getcwd()  # This is how you get the current working directory
    print(cur_dir)
    print(
        os.path.split(cur_dir)
    )  # splits the leaf level of the path from the parent path
    print(os.path.dirname(cur_dir))  # returns teh parent path
    print(os.path.basename(cur_dir))  # returns the leaf level of the path
    while os.path.basename(cur_dir):
        """
        This loop will walk up a directory tree until it reaches the root directory.
        """
        cur_dir = os.path.dirname(cur_dir)
        print(cur_dir)


def find_rc(
    rc_name=".examplecr",
):  # You can rewrite this function using pathlib rather than os.path but eh I'm lazy
    # Check for Env variable
    var_name = "EXAMPLERC_DIR"
    if (
        var_name in os.environ
    ):  # This is how you check if an environment variable exists
        var_path = os.path.join(
            f"${var_name}", rc_name
        )  # Use join to construct a path with the environment variable. This will look something like $EXAMPLERC_DIR/.examplerc
        config_path = os.path.expandvars(
            var_path
        )  # Expand the environment variable to insert its value into the path
        print(f"Checking {config_path}")
        if os.path.exists(config_path):  # Check to see if the file exists
            return config_path

    # Check the current working directory
    config_path = os.path.join(
        os.getcwd(), rc_name
    )  # Construct a path using the current working directory
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # Check the user's home directory
    home_dir = os.path.expanduser(
        "~/"
    )  # Use the expanduser function to get the path to the user's home directory
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # Check Directory of This file
    file_path = os.path.abspath(
        __file__
    )  # Expand the relative path stored in file to an absolute path
    parent_path = os.path.dirname(
        file_path
    )  # Use dirname to get the path to the directory holding the current file
    config_path = os.path.join(parent_path, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    print(f"File {rc_name} has not been found")


"""
The path submodule also offers ways to interrogate stats about a path.
You can determine if a path is a file, a directory, a link, or a mount. You can get stats such as it's size or time of last access of modification.
"""


def walk_path(parent_path):
    """
    You could use a script like this to identify large files or files that have not been accessed and then report, move, or delete them
    """

    print(f"Checking: {parent_path}")
    childs = os.listdir(parent_path)  # os.listdir returns the contents of a directory

    for child in childs:
        child_path = os.path.join(
            parent_path, child
        )  # Construct the full path of an item in the parent directory
        if os.path.isfile(child_path):  # Check to see if the path represents a file
            last_access = os.path.getatime(
                child_path
            )  # Get the last time the file was accessed
            size = os.path.getsize(child_path)  # Get the size of the file
            print(f"File: {child_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")
        elif os.path.isdir(child_path):  # Check if the path represents a directory
            walk_path(child_path)  # Check the tree from this directory down

    if __name__ == "__main__":
        fire.Fire()


"""
The os module offers a convenience function for walking directory trees calles os.walk.
This function returns a generator that in turn returns a tuple for each iteration.
The tuple consists of the current path, a list of directories, and a list of files.
"""


def walk_path(parent_path):
    for parent_path, directories, files in os.walk(parent_path):
        print(f"Checking: {parent_path}")
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access = os.path.getatime(file_path)
            size = os.path.getsize(file_path)
            print(f"File: {file_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")
