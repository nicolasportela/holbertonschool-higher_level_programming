#!/usr/bin/python3
for n in range(48, 58):
    for nn in range(48, 58):
        if n == 57 and nn == 57:
            print("{:c}{:c}".format(n, nn))
        else:
            print("{:c}{:c}, ".format(n, nn), end="")
