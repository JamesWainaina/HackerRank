#!/usr/bin/python3


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0

        while i < len(nums):
            if nums[i] != i + 1:
                correct = nums[i] - 1
                if nums[i] != nums[correct]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                else:
                    return nums[i]
            else:
                i += 1
        else:
            return -1
        

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 1, 3, 4, 2]  # Example input with a duplicate
    print("Duplicate number is:", solution.findDuplicate(nums))