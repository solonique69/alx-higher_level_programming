#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def _abs(num):
    if num < 0:
        return -num
    else:
        return num


remainder = (_abs(number) % 10)

if number < 0:
    remainder = -1 * remainder


print(f"Last digit of {number} is {remainder}", end=" ")
if remainder > 5:
    print("and is greater than 5")
elif remainder == 0:
    print("and is 0")
elif remainder < 6 and remainder != 0:
    print("and is less than 6 and not 0")
