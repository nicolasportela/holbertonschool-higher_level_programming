#!/usr/bin/python3
from variable_load_5 import a
if __name__ == "__main__":
    astr = str(a)
    for i in range(len(astr)):
        print("{:s}".format(astr[i]), end="")
    print()
