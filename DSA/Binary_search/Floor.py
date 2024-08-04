#!/usr/bin/python3
"""
calculating the floor of a number
"""

def floor(arr, target):
    if target > arr[-1]:
        return -1
    
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]
    
    return arr[end] if end >= 0 else -1

arr = [1, 2, 8, 10, 10, 12, 19]
target = 5
print(floor(arr, target))