#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        result = ""
        if i != n:
            result += str[i]
            print(result, end='')
    print('')
    exit()
