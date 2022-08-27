""" 
It is better to be in a virtual environment when downloading special packages so you don't mess up certain dependencies especially on linux
In order to do that type:
    $python -m venv venv      //This creates a virtual environment with the name venv
    $source venv/bin/activate //This activates the virtual environment
"""


def HelloWorld():
    print("Hello World")
    return


def BuiltInRange():
    print(
        range(10), list(range(10)), list(range(5, 10)), list(range(5, 10, 3))
    )  # range(i,j,k) gives you a range of numbers, i is the starting val, j is the ending val and is NOT included, k is how many steps you take
    return


def Exceptions():
    thinkers = ["Plato", "PlayDo", "Gumby"]
    while True:
        try:
            thinker = (
                thinkers.pop()
            )  # pop() takes the last element of your list and removes that one
            print(thinker)
        except IndexError as e:
            print("We tried to pop too many thinkers")
            print(e)
            break


def SimpleListCompr():
    square = [i**2 for i in range(10)]
    print(square)
    return


def Strip():
    input = "     I want more     "
    print(input.strip(), input.lstrip(), input.rstrip())  # strip() removes whitespaces
    return


def Split():
    text = "Mary had a little lamb"
    print(
        text.split()
    )  # split() breaks a string into its components and returns a list
    url = "gt.motomomo.io/v2/api/asset/143"
    print(
        url.split("/")
    )  # uses whitespaces by default but can also use different characters
    return


def count():
    n = 0
    while True:
        n += 1
        yield n  # basically yield is just a fancy return, everytime our function (here specifically it is a generator) it returns the value specified by yield and then pauses its state until it is next called


def fibonacci_generator():
    first = 0
    last = 1
    while True:
        first, last = last, first + last
        yield first


"""
In the book there is an interesting part at the end of this chapter regarding the IPython interpreter and how you can use it to execute shell command.
In order to use native python to execute shell commands, you should prolly just use the library os which comes with a lot of stuff regarding your system and how to control it with python scripts.
"""


def Exercise_1(name):
    """
    Exercise was to write a function that takes a name and prints name.
    Could be improved by checking if name is empty or not and/or if the name is a string or not.
    """
    print(name)
    return


def Exercise_2(string):
    """
    Exercise was to write a function that takes a string and prints out wether it is upper or lower case.
    Was improved by adding the case that if the name both contains upper and lower case chars that it prints out neither.
    Could be improved by ideas mentioned in Exercise_1().
    """
    if string.isupper():
        print("upper")
        return
    elif string.islower():
        print("lower")
        return
    print("neither")
    return


def Exercise_3():
    """
    Exercise was to write a function that takes the string "smog-tether" and inserts that string into a list with the string all capitalized.
    Could be improved by ideas mentioned in Exercise_1().
    """
    string = "smog-tether"
    list = [x.upper() for x in string]
    print(list)


def Exercise_4():
    """
    Exercise was to write a generator that alternates between even and odd.
    """
    n = 0
    while True:
        if n % 2 == 0:
            n += 1
            yield "even"
        else:
            n += 1
            yield "odd"
