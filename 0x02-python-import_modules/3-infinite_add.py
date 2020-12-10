#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    if len(argv) == 1:
        print("0")
    if len(argv) > 1:
        for i in range(1, len(argv)):
            argvi = int(argv[i], 10)
            sum = sum + argvi
        print("{:d}".format(sum))
