#!/usr/bin/python3

"""
Order Agnostic Binary Search
"""

def order_agnostic_binary_search(arr, target):
    if not arr:
        return -1
    
    start, end  = 0, len(arr) - 1
    isAscending = arr[start] < arr[end]

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        
        if isAscending:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1

# Example usage:
arr1 = [1, 3, 5, 7, 9, 11]  # Ascending order
arr2 = [20, 15, 10, 5, 0]    # Descending order

print(order_agnostic_binary_search(arr1, 7))  # Output: 3
print(order_agnostic_binary_search(arr2, 5))