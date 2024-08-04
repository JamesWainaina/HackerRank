#!/usr/bin/python3
from typing import List

class SetMismatch:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] =  nums[correct], nums[i]
            else:
                i += 1
        
        for index in range(len(nums)):
            if nums[index] != index + 1:
                return [nums[index], index + 1]
        else:
            return [-1, -1]
        
if __name__ == "__main__":
    solution = SetMismatch()
    nums = [1, 2, 2, 4]  # Example input with a duplicate
    print("Duplicate number is:", solution.findErrorNums(nums))
        