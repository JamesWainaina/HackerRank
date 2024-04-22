#!/usr/bin/python3
"""
write a fuction to reverse a string using recursion"""

def reversrString(s):
    if len(s) == 0:
        return s
    return reversrString(s[1:]) + s[0]
print(reversrString("james learning"))  