#!/usr/bin/python3

"""
2_D_Arrays also known as a matix or a grid.

finding the maximum hourglass sum in a matrix
hourglass_sum is the maximum elements in the matrix
eg: the pattern
    a b c
      d
    e f g
task:
    printing the largest (maximum) hourglass sum foud in A.
"""

import sys

def get_hourglass_sum(matrix, row, col):
    sum = 0

    # getting the seven elements that make up a sum
    sum += matrix[row - 1][col - 1] # element above it to the left.
    sum += matrix[row - 1][col] # element directly above it
    sum += matrix[row - 1][col + 1] # element above it to the right.
    sum += matrix[row][col] # The exact element.
    # element below it
    sum += matrix[row + 1][col - 1] # element below it to the right
    sum += matrix[row + 1][col] # direct element below it
    sum += matrix[row + 1][col + 1] # element below it to the left
    return sum


arr = []

for arr_i in range():
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

max_hourglass_sum = -63 # sum of all negative nines 

# n/b you should initiliaze the max_hourglass_sum to be minimum possible sum

for i in range(1, 5): # iterating through second to fourth row
    for j in range(1, 5): # iterating through second to fourthcol 

        current_hourglass_sum = get_hourglass_sum(arr, i, j)
        
        if current_hourglass_sum > max_hourglass_sum:
            max_hourglass_sum = current_hourglass_sum
print(max_hourglass_sum)