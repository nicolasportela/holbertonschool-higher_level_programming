#!/usr/bin/python3
for n in range(100):
    if n == 99:
        print("{:d}".format(n))
    else:
        print("{:d}, ".format(n), end="")
