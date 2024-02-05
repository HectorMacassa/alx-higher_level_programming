#!/usr/bin/python3
"""This module defines a MyList class"""


class MyList(list):
    """This class inherits from list class"""

    def print_sorted(self):
        """Prints a sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
