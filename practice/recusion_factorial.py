#!/usr/bin/python3

"""
Write a factorial fuction that takes a positive integer N as a parameter and 
prints the result of N(N factorial).
"""

import sys

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)