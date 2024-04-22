#!/usr/bin/python3
"""
write a function that calculates the total number of swaps in a bubble sort algorithm
efficincy of the algorithm is o(n^2)
"""
import sys

n = int(input().strip())
a = list(map(int, input().strip()))  # Read the entire line as a string and split it into characters

totalNumberOfSwaps = 0

for i in range(n):
    numberOfSwaps = 0
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            tmp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = tmp
            numberOfSwaps += 1
    totalNumberOfSwaps += numberOfSwaps

    if numberOfSwaps == 0:
        break

print("Array is sorted in " + str(totalNumberOfSwaps) + ' swaps')
print("First element: " + str(a[0]))
print("Last element: " + str(a[n - 1]))
