#!/usr/bin/python3
import math

"""
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Given a number, n, determine and print whether it's prime or not prime.
"""
 

def isprime(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False
    for i in range(2, int(sqrt_n) + 1):
        if n % i == 0:
            return False
    return True

number_test_cases = int(input())

for i in range(number_test_cases):
    n = int(input())
    if isprime(n):
        print('prime')
    else:
        print('not prime')

    
    