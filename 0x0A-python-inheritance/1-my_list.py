#!/usr/bin/python3


"""Class MyList that inherits from list"""


class MyList(list):

    """Public instance method that prints the list sorted (ascending)"""

    def print_sorted(self):

        """all elements will be type int"""
        if issubclass(MyList, list):
            print(sorted(self))
