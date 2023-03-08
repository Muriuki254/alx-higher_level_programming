#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if (i == 8 and j == 9):
            print("{0:d}{1:d}".format(i, j))
            break
        if not (j == i or i > j):
            print("{0:d}{1:d}".format(i, j), end=', ')
