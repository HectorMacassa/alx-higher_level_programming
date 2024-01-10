#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        my_list = []

    multiples_of_2 = [num % 2 == 0 for num in my_list]
    return multiples_of_2
