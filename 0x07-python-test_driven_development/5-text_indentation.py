#!/usr/bin/python3
"""
This module contains a function
which prints a text with 2 new lines
after any of these characters: ., ? and :
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    n_l = list(text)
    for i in range(len(n_l)):
        if n_l[i] is ".":
            n_l[i + 1] = '\n\n'
        if n_l[i] is "?":
            n_l[i + 1] = '\n\n'
        if n_l[i] is ":":
            n_l[i + 1] = '\n\n'
    n_t = ""
    n_t = n_t.join(n_l)
    print("{}".format(n_t), end="")
