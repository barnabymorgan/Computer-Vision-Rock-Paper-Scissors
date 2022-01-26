from random import randint


def comp_guess():
    for _ in range(10):
        value = randint(0, 2)
        print(value)


comp_guess()
