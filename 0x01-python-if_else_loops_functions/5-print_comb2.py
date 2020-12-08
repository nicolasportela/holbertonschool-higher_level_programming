#!/usr/bin/python3
for n in range(0, 10):
    print("0{:d}, ".format(n), end="")
for n in range(10, 100):
    if n < 99:
        print("{:d}, ".format(n), end="")
    elif n == 99:
        print("{:d}".format(n))
