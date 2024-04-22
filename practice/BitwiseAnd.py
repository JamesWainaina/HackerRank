#!/usr/bin/python3

"""
Given set S = {1, 2, 3, ...N}. Find two integers, A and B(where A < B) from set s such that the 
valu of A & B is the maximum possible and also less than a given integer, K.In this case, & 
represents the bitwise AND operator. 
"""

import math
import os
import random
import re
import sys

def find_max_bitwise(n, k):
    max_bitwise = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            bitwise = i & j
            if max_bitwise < bitwise < k:
                max_bitwise = bitwise
                if max_bitwise == k - 1:
                    return max_bitwise

    return max_bitwise

if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])
        k = int(nk[1])

        print(find_max_bitwise(n, k))