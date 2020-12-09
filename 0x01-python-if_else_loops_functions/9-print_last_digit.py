#!/usr/bin/python3
def print_last_digit(number):
    absolute = abs(number)
    print("{:d}".format(absolute % 10), end="")
    return(absolute % 10)
