#!/usr/bin/python3
def islower(c):
    for chr in range(97, 123):
        if ord(c) == chr:
            return True
    else:
        return False
