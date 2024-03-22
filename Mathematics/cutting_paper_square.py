#!/usr/bin/python3

import math
import os
import random
import re
import sys


"""
Mary has an n * m piece of paper that she wants to cut 
into 1 * 1 pieces according to the following rules:

She can only cut one piece of paper at a time, 
meaning she cannot fold the paper or layer 
already-cut pieces on top of one another.
Each cut is a straight line from one side of the paper 
to the other side of the paper.

For example, the diagram below depicts 
the three possible ways to cut a 3 * 2 piece of paper:

Given n and m, 
find and print the minimum number of cuts Mary 
must make to cut the paper into n.m squares 
that are 1 * 1 unit in size.

#Input Format

A single line of two space-separated integers 
denoting the respective values of n and m.
"""

def solve(n, m):
    # Since MARY wants to cut the paper into individual 1 * 1 
    # she will need one cut less than the total number of squares.This is because each cut creates two adjacent squares
    return n * m - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
