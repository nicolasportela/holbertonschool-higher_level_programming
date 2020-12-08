#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        asc = ord(str[c])
        if asc > 96 and asc < 123:
            asc = asc - 32
        print('{:c}'.format(asc), end="")
    print()
