#!/usr/bin/python3
def uppercase(str):
    for chr in str:
        if ord(chr) >= ord('a') and ord(chr) <= ord('z'):
            conv = ord(chr) - 32
        else:
            conv = ord(chr)
        print("{:c}".format(conv), end='')
    print('')
