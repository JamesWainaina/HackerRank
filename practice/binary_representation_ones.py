#!/usr/bin/python3

"""
Given a base 10 integer, n , convert it to binary(base 2). 
Then find and print base 10 integer denoting the maximum number of consecutive 1's in n's 
binary represntation.

converting a number into binary find the numbers remainder by dividing by 2 or n(log 2) then,
dividing the integer by two and rounding down.

5 log2 is 1 = 1 is lowest power of 2 in our binary conversion.
then 5 divided by 2 = 2.5, round down to 2 there is no remainder when 2 is divided by 2 = 0
we have 1,0 as our binary representation
then 2 divided by 2 = 1 
no remainder so we have 101 as our binary represenation.
then 1 divided by 2 = 0.5, finished converting to binary result = 1010

we should find the maximum number of consequtive once.we will keep a counter of the current number
of consequtive one's and a counter of the maximum number of consequtive one's.Everytime we 
see that the remainder is 1 ,we will increment the current number of consequtive one's. If the current
number of consequtive ones' is greater the maximum numer of consequtive ones we will set that to the 
maximum number of consequtive ones ,if we get a remainder of 0 our chain number of consequtive ones is
broken so we will reset that value to 0.
"""

import sys

n = int(input().strip())

current_consecutive_1s = 0
max_consecutive_1s = 0

while n > 0:
    remainder = n % 2
    if remainder == 1:
        current_consecutive_1s += 1
        if current_consecutive_1s > max_consecutive_1s:
            max_consecutive_1s = current_consecutive_1s
    else:
        current_consecutive_1s = 0
    n = n // 2 # dividing n until its fully converted to binary.

print(max_consecutive_1s)


 