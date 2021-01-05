#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    try:
        for count in range(x):
            print("{}" .format(my_list[count]), end="")
            total = total + 1
    except:
        pass
    print()
    return total
