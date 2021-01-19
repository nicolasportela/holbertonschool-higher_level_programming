#!/usr/bin/python3
"""
This module contains a function
which prints a text with 2 new lines
after any of these characters: ., ? and :
"""


def text_indentation(text):
    """The function takes a string and prints it, replacing each period (.),
    double colon (:) and question mark (?) for two empty lines.
    Args:
        text (str): text to be printed
    Raises:
        TypeError: when text is not a string"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    n_l = list(text)
    for i in range(len(n_l)):
        if n_l[i] is ".":
            if n_l[i + 1] == " ":
                n_l[i + 1] = '\n\n'
            else:
                n_l[(i + 1):(i + 1)] = '\n\n'
        if n_l[i] is "?":
            if n_l[i + 1] == " ":
                n_l[i + 1] = '\n\n'
            else:
                n_l[(i + 1):(i + 1)] = '\n\n'
        if n_l[i] is ":":
            if n_l[i + 1] == " ":
                n_l[i + 1] = '\n\n'
            else:
                n_l[(i + 1):(i + 1)] = '\n\n'
    n_t = ""
    n_t = n_t.join(n_l)
    print("{}".format(n_t), end="")
