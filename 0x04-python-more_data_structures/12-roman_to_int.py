#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    chars = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0

    if len(roman_string) == 1:
        for a, b in chars.items():
            if roman_string[0] == a:
                return b

    for a in range(len(roman_string)):
        for i in chars:
            if i == roman_string[a]:
                break

    str_list = []

    for i in roman_string:
        for a, b in chars.items():
            if i == a:
                str_list.append(b)

    for i in range(len(str_list)):
        res = res + str_list[i]
        if i > 0:
            if str_list[i - 1] < str_list[i]:
                res = res - (str_list[i - 1] * 2)
    return res
