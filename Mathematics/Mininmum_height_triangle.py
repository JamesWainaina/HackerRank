#!/usr/bin/python3

import math
import os
import random
import re
import sys

"""
Given integers b and a, find the smallest integer h,
such that there exists a triangle of height h,
base b , having an area of at least a.

Example
b = 4
a = 6
The minimum height h is 3. 
One example is a triangle formed 
at points (0, 0), (4, 0), (2, 3).

Function Description

Complete the lowestTriangle function in the editor below.

lowestTriangle has the following parameters:

int b: the base of the triangle
int a: the minimum area of the triangle
Returns

int: the minimum integer height to 
form a triangle with an area of at least a

Input Format

There are two space-separated integers b and a,
on a single line.
"""

def lowestTriangle(trianglebase, area):
    

    return math.ceil(2 * area / trianglebase)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    trianglebase = int(first_multiple_input[0])

    area = int(first_multiple_input[1])

    height = lowestTriangle(trianglebase, area)

    print(height)
