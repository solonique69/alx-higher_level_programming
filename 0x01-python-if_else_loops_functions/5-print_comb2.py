#!/usr/bin/python3

for x in range(0, 100):
        if x < 10:
                print("0{}".format(x), end=", ")
        elif x > 9:
                print("{}".format(x), end=", ")
        if x == 99:
                print("{}".format(x))
