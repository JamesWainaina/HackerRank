#!/usr/bin/python3

import math
import os
import random
import re
import sys

"""
Cities on a map are connected by a number of roads.
The number of roads between each city is in an array 
and city 0 is the starting location. 
The number of roads from city 0 to city 1 is the
first value in the array, 
from city 1 to city 2 is the second, and so on.

How many paths are there from city 0 
to the last city in the list, modulo  1234567?

Example
n = 4
routes = [3,4,5]

There are 3 roads to city 1,4 roads 1 to city 2 and 5 roads to city 3. 
The total number of roads is 
3 * 4 * 5 mod 1234567 = 60

Note
Pass all the towns Ti for i=1 to n-1 in numerical order 
to reach Tn.

#Function Description

Complete the connectingTowns function in the editor below.

connectingTowns has the following parameters:

int n: the number of towns
int routes[n-1]: the number of routes between towns

#Returns

int: the total number of routes, modulo 1234567.

#Input Format
The first line contains an integer T, T test-cases follow.

Each test-case has 2 lines.
The first line contains an integer N (the number of towns).
The second line contains N - 1 space separated integers 
where the ith integer denotes the number of routes, Ni, from the town Ti to Ti+1
"""

def connectingTowns(n, routes):
    total_routes = 1  # initializing the count for total_routes
    for route in routes:
        total_routes *= route
        total_routes %= 1234567  # Makes the result to remain within the specified problem
    return total_routes
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()
