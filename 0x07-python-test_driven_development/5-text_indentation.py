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

    newlist = list(text)
    for i in range(len(newlist)):
        if newlist[i] is "." or newlist[i] is "?" or newlist[i] is ":":
            if newlist[i + 1] == " ":
                newlist[i + 1] = '\n\n'
            else:
                newlist[(i + 1):(i + 1)] = '\n\n'
    newtext = ""
    newtext = newtext.join(newlist)
    print("{}".format(newtext), end="")
