#!/usr/bin/python3

"""Write a calculator class witha single method in power[int, int].The power method takes two integers
,n and p, as parameters and return s the integer result of n * p. if either p or n are negative, then
the method most nust throw an exception with the message: n and p should be non-negative"""

import os


class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            print("n and p should be non-negative")
        else:
            power = pow(n, p)
            print(power)

mycalculator = Calculator()
t = int(input())
for i in range(t):
    n, p = map(int, input().split())
    try:
        ans = mycalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)