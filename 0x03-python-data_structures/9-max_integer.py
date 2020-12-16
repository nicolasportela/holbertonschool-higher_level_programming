#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i > 0:
            if i > (i - 1):
                maxi = i
        else:
            i += 1
    return maxi
