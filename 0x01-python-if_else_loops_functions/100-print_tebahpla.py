#!/usr/bin/python3
for n in range(122, 96, -1):
    if n % 2 is 0:
        l = n
    elif n % 2 is 1:
        l = n - 32
    print("{:c}".format(l), end="")
