#!/usr/bin/python3

class Solution:
    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr) - 1

        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start

solution = Solution()
arr = [1, 3, 5, 7, 6, 4, 2]
print(solution.peakIndexInMountainArray(arr))

"""
Also solves question 162 for finding peak Element in an array
"""