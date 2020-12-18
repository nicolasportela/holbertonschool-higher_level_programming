#!/usr/bin/paython3
def print_sorted_dictionary(a_dictionary):
    sor = sorted(a_dictionary.keys())
    for a, b in sor:
        print("{}: {}".format(a, b))
