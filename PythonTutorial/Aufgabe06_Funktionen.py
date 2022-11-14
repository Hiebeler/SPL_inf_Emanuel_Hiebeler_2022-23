from random import randrange


def addTwoNumbers(a, b):
    return a + b


print(addTwoNumbers(1, 3))


def randomNumber():
    return randrange(100) + 100


print(randomNumber())


def Word(stringArray):
    return stringArray[randrange(len(stringArray))]


print(Word(["halloo", "moin"]))
