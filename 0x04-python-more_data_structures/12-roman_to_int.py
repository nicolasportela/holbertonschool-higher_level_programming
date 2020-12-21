#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    flag = 1

    if len(roman_string) == 1:
        for a, b in values.items():
            if roman_string[0] == a:
                return b

    for a in range(len(roman_string)):
        for i in values:
            if i == roman_string[a]:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            return 0

    str_list = []

    for i in roman_string:
        for a, b in values.items():
            if i == a:
                str_list.append(b)

    for i in range(len(str_list)):
        sum = sum + str_list[i]
        if i > 0:
            if str_list[i - 1] < str_list[i]:
                sum = sum - (str_list[i - 1] * 2)
    return sum
