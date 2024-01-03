#!/usr/bin/python3
def remove_char_at(str, n):
    rm = ''
    i = 0
    for char in str:
        if i != n:
            rm += str[i]
        i += 1
    return (rm)
