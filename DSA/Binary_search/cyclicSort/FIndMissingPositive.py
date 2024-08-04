#!/usr/bin/python3
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            correct = nums[i] - 1
            if 0 <= correct < len(nums) and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

            for index in range(len(nums)):
                if nums[index] != index + 1:
                    return index + 1
            return len(nums) + 1
        
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 4, -1, 1]  # Example input with some numbers missing
    print("Missing number is:", solution.firstMissingPositive(nums))