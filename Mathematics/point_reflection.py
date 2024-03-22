#!/usr/bin/python3

import math
import os
import random
import re
import sys

"""Consider two points, p = (px,py) and q = (qx, qy) .
We consider the inversion or point reflection,r = (rx,ry),
of point p across point q to be a 180 degress
rotation of point p around q.

Given n sets of points p and q, find r for each pair of 
points and print two space-separated integers 
denoting the respective values of rx  and ry  
on a new line.

Function Description

Complete the findPoint function in the editor below.

findPoint has the following parameters:

int px, py, qx, qy: x and y coordinates for points p and q 
Returns

int[2]: x and y coordinates of the reflected point r
"""

def findPoint(px, py, qx, qy):

    # calculate the difference between the coordinates of p and q
    diff_x = qx - px
    diff_y = qy - py

    # calculate the coordinates of r using the inversion or point reflection
    rx = qx + diff_x
    ry = qy + diff_y
    
    # Return the coordinates of r as a list
    return [rx, ry]
    

if __name__ == '__main__':
    # read the number of sets of points

    n = int(input().strip())

    #Iterate through each set of points
    for n_itr in range(n):
        # Read the coordinates of points p and q for each test case
        px, py, qx, qy = map(int, input().strip().split())

        # Call the findPoint function to get the coordinates of point r
        result = findPoint(px, py, qx, qy)

        print(''.join(map(str, result)))
