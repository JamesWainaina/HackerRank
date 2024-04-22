#!/usr/bin/python3

"""Given an array A of N intergers, print As elements in reverse order as
 a single space-seperated numbers"""

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

reversed_array = arr[::-1]

output_string = ' '.join(map(str, reversed_array))

print(output_string)