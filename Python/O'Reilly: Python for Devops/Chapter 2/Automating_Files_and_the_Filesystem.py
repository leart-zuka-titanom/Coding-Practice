import pathlib
import json
from pprint import pprint

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
    )  # This is the function that essentially opens the file. By default, the mode will be read, but you can also choose to write the file by givin 'w' as the argument
    text = (
        open_file.read()
    )  # This reads the file as a whole. You also have the option to use .readlines() in order to read the file line by line, which will also have an effect on how the file will be treated.
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
    ) as opened_file:  # The open function creates a file if it does not already exist and overwrites if it does. If you want to simply append to the file, use the append flag a
        opened_file.write(
            text
        )  # Basically the same as open. The \n in the message was added so that when you simply print the content of the file via cat the shell prompt is being printed in the next line.


def file_handler_pathlib_read():
    path = pathlib.Path(
        "/home/leart/Learnding/Python/O'Reilly: Python for Devops/Chapter 2/Message"
    )  # Appareantly you have to give the full path lul
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
        policy = json.dump(
            policy, opened_file
        )  # In order to then write json files you can use the function dump()
        pprint(policy)

"""
The book now talks about some other languages used in configuration files like YAML or languages used in data serialization like XML.
I will not talk about them here since first I've never used them and second if I feel the need to learn them I will do so in the future.
(Call me lazy ion care)
"""
