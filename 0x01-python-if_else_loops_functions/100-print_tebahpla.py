#!/usr/bin/python3
for alphabet in range(26):
    if alphabet % 2 == 0:
        print("{:c}".format(122 - alphabet), end="")
    else:
        print("{:c}".format(90 - alphabet), end="")
