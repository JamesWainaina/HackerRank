#!/usr/bin/python3

import math
import os
import random
import re
import sys

"""
Luke is daydreaming in Math class. He has a sheet of graph paper
with  n rows and m columns, and he imagines that there is an army base in each 
cell for a total of n.m bases. He wants to drop supplies
at strategic points on the sheet, marking each drop point with a red dot. 
If a base contains at least one package inside or on top of its border fence,
then it's considered to be supplied.

Given n and m, what's the minimum number of packages 
that Luke must drop to supply all of his bases?

Example
n = 2
m = 3
Packages can be dropped at the corner between cells
(0, 0), (0, 1), (1, 0) and (1, 1) to supply 4 bases. 
Another package can be dropped at a border between 
(0, 2) and (1, 2). This supplies all bases using 
2 packages.

#Function Description

Complete the gameWithCells function in the editor below.

gameWithCells has the following parameters:

int n: the number of rows in the game
int m: the number of columns in the game
Returns

int: the minimum number of packages required

#Input Format

Two space-separated integers describing 
the respective values of n and m.
"""

def gameWithCells(n, m):
    # Calculate the number of packages required to cover all bases
    # Each package covers 4 bases (corner of each cell)
    
    packages = (n // 2) * (m // 2)

    # Check if there are leftover rows or columns

    if n % 2 == 1:
        packages += m // 2 # Add extra packages to cover the remaining bases in the last row
    if m % 2 == 1:
        packages += n // 2 # Add extra packages to cover the remaining base in the last column

    # If both n and m are odd, we need one more package to cover the corner base
    if n % 2 == 1 and m % 2 == 1:
        packages += 1

    return packages

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
