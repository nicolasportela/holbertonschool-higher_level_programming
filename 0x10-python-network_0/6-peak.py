#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if len(list_of_integers) < 3:
        return None
    if len(list_of_integers) == 3:
        return list_of_integers[2]
    else:
        return max(list_of_integers[1:-1])
