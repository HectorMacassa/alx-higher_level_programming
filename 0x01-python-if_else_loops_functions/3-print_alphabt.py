#!/usr/bin/python3
for alphabet in range(97, 123):
    if alphabet == 101:
        continue
    elif alphabet == 113:
        continue
    else:
        print("{}".format(chr(alphabet)), end="")
