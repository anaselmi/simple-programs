from random import randint
from functools import reduce


def dice_roll(*args):
    for roll in args:
        roll = roll.split("d")
        amount = int(roll[0])
        faces = int(roll[1])
        total = reduce(lambda x, _: x + randint(0, faces), range(0, amount))
        print(total)
