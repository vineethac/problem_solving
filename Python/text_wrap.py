'''
You are given a string and width .
Your task is to wrap the string into a paragraph of width

Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''

import textwrap

def wrap(string: str, max_width: int) -> str:
    new_string = ""
    j = 0
    for i in string:
        new_string += i
        j += 1
        if j == max_width:
            new_string += '\n'
            j = 0
    return new_string
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)