#!/usr/bin/python3
"""
This module defines a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using
    the divide-and-conquer approach.
    """
    def find_peak_util(arr, low, high):
        if low == high:
            return low

        mid = low + (high - low) // 2

        if (mid == 0 or arr[mid] >= arr[mid - 1]) and \
           (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return mid

        if mid > 0 and arr[mid - 1] > arr[mid]:
            return find_peak_util(arr, low, mid - 1)

        return find_peak_util(arr, mid + 1, high)

    if not list_of_integers:
        return None
    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1)
