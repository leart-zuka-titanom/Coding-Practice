import pytest

"""
It is better to be in a virtual environment when downloading special packages, so you don't mess up certain dependencies, 
especially on linux where sometimes having too many dependencies is a cause of frustration and new installation of the entire system : ^).
In order to do that type:
    $python -m venv venv      //This creates a virtual environment with the name venv
    $source venv/bin/activate //This activates the virtual environment
Please for the love of god don't commit this folder to GitHub
"""

"""
The pytest framework makes it easy to write small, readable tests, and can scale to support functional testing for 
applications and libraries. 

In order to run pytest run:
    $python -m pytest
this will look for files with the name test_*.py and run them.

The output will be a summary of the tests that were run and whether they passed or failed.

It can be too verbose from time to time so in order to control the output, 
you can use the -q flag to only show the summary.
On the other hand, if you're a maniac, you can use then -v flag to show the output of each test.

Certain conventions are used to name tests:
    - The testing directory needs to be names tests
    - The tiles need to be prefixed with test; i.e. test_basic.py, or suffixed with test.py
    - Test functions need to be prefixed with test_; i.e. def testsimple():
    - Test classes need to be prefixed with Test; i.e. class TestSimple:
    - Test methods follow the same conventions as functions, prefixed with test_: i.e. def test_method():
    
What's also quite funny is that pytest similar to neovim or fish also supports plugins which can help you write tests or spice up the look of pytest.
If you want to have a look at the available plugins (currently 1007), have a lok at https://docs.pytest.org/en/7.1.x/reference/plugin_list.html.
"""


def test_simple():
    assert True


def test_fails():
    assert False


def test_long_lines():
    assert "using assert for errors" == "using asert for errors"


def test_long_lists():
    assert ["a", "very", "long", "list", "of", "words"] == [
        "a",
        "very",
        "long",
        "list",
        "items",
    ]


"""
The book now goes into the concept of Parameterized Tests and why they are useful.

Let's say you have a function that takes an input and returns True if it is implying a truthful value.
"""


def string_to_bool(string):
    return bool(string)


"""
Now let's say we want to test a bunch of different inputs and see if they are all True.
"""


def test_many_inputs():
    assert string_to_bool("yes")  # detects lower case

    assert string_to_bool("YeS")  # detects odd case

    assert string_to_bool("YES")  # detects upper case

    assert string_to_bool("1")  # detects positive str int

    assert string_to_bool("true")  # detects true

    assert string_to_bool("true ")  # detects trailing space

    assert string_to_bool(" true")  # detects leading space


"""
This test will pass no problem whatsoever but it is without a doubt fucking retarded to write such a test.

This is where parametrization comes into play.
"""

true_values = ["yes", "1", "Yes", "TRUE", "TruE", "True", "true"]


@pytest.mark.parametrize(
    "value", true_values
)  # Here we're telling pytest that value is the name to sue for the argument in the test method
def test_it_detects_truish_strings(value):
    assert string_to_bool(value)


"""
What this will do is hand off all of the values that are in my list to the function itself and treat every single 
value as its own test.
"""
# TODO: Continue reading chapter 8 where concepts like fixtures and infrastructure tests are being explained
