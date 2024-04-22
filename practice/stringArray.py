#!/usr/bin/python3

"""Read a string S, and print as integer value, if S cannot be converted to an integer
print bad string"""

import os

s = input().strip()

try:
    int_conv = int(s)
    print(int_conv)
except ValueError:
    print("Bad String")

