#!/usr/bin/python3

import math
import os
import random
import re
import sys


"""
Leonardo loves primes and created q queries
where each query takes the form of an integer,n .
For each n, count the maximum number of distinct 
prime factors of any number in the inclusive range [1, n].

Note: Recall that a prime number is only divisible by 1 
and itself, and 1 is not a prime number.

Example
n = 100

The maximum number of distinct prime factors 
for values less than or equal to 100 is 3. 
One value with 3 distinct prime factors is 30 .
Another is 42.

#Function Description

Complete the primeCount function in the editor below.

primeCount has the following parameters:

int n: the inclusive limit of the range to check

#Returns

int: the maximum number of distinct prime factors
of any number in the inclusive range [0 - n].

#Input Format

The first line contains an integer,q,
the number of queries.
Each of the next q lines contains a single integer, n.
"""

def primeCount(n):
    factor = 0 # used to count the number of prime factors
    prime = 2 # used to iterate through potential prime numbers
    isPrime = True # used to check if a number is prime or not
    prod = 1 # store the product of prime factors encountered.
    
    while(True):
        for i in range(2, prime): # iterates from 2 which is a prime to the current prime number
            if prime % i == 0: # checks if prime isPrime by checking if it is divisible by any number from 2 to prime - 1.
                isPrime = False 
        if isPrime: 
            prod = prod * prime
            factor += 1 # increses the number of prime factors
            if prod > n: # if prime exceeds n it decrements it by 1.
                factor -= 1 
                break
        prime += 1 # Regardless of whether prime isPrime or not 
        isPrime = True # It icrements prime by 1 and resets isPrime to True for the next iteration.
    return (factor)

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        print(result)
