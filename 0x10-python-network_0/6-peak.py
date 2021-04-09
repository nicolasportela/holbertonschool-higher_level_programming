#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """function to return a peak number"""

    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)

    half_nodec = int(n / 2)
    half_num = list_of_integers[half_nodec]

    if half_num > list_of_integers[half_nodec - 1] and \
       half_num > list_of_integers[half_nodec + 1]:
        return half_num
    elif half_num < list_of_integers[half_nodec - 1]:
        return find_peak(list_of_integers[:half_nodec])
    else:
        return find_peak(list_of_integers[half_nodec + 1:])
