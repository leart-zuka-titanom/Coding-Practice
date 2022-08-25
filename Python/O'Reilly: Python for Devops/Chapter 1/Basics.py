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
