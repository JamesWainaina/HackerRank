#!/usr/bin/python3

class MountainArray:
    def __init__(self, arr):
        self._arr = arr

    def get(self, index: int) -> int:
        return self._arr[index]

    def length(self) -> int:
        return len(self._arr)

class Solution:
    def findInMountainArray(self, target: int, mountainArr: MountainArray) -> int:
        peak = self.peakIndexInMountainArray(mountainArr)
        firstTry = self.orderAgnosticBinarySearch(mountainArr, target, 0, peak)

        # If target is found in the ascending part
        if firstTry != -1:
            return firstTry
        
        # Search in the descending part
        return self.orderAgnosticBinarySearch(mountainArr, target, peak + 1, mountainArr.length() - 1)

    def peakIndexInMountainArray(self, mountainArr: MountainArray) -> int:
        start = 0
        end = mountainArr.length() - 1

        while start < end:
            mid = (start + end) // 2
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                # We are in the descending part of the array
                end = mid
            else:
                # We are in the ascending part of the array
                start = mid + 1
        # Start and end converge to the peak index
        return start

    def orderAgnosticBinarySearch(self, mountainArr: MountainArray, target: int, start: int, end: int) -> int:
        isAscending = mountainArr.get(start) < mountainArr.get(end)
        while start <= end:
            mid = (start + end) // 2
            midValue = mountainArr.get(mid)

            if midValue == target:
                return mid

            if isAscending:
                if midValue > target:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if midValue < target:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1  # Target not found

mountain_arr = MountainArray([1, 2, 3, 4, 5, 3, 1])
solution = Solution()
target_index = solution.findInMountainArray(3, mountain_arr)
print(target_index)  # Outputs the index of the target in the mountain array
