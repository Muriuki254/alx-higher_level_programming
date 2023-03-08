#!/usr/bin/python3
for alpha in reversed(range(97, 123)):
    if alpha % 2 == 1:
        conv = alpha - 32
    else:
        conv = alpha
    print("{:c}".format(conv), end='')
