#!/usr/bin/python3
for n in range(10):
    for nn in range(10):
        if n < nn:
            if n is 8 and nn is 9:
                print("{:d}{:d}".format(n, nn))
            else:
                print("{:d}{:d}".format(n, nn), end=", ")
