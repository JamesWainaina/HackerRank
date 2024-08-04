#!/usr/bin/python3

class Solution(object):
    def findDisappearedNumbers(self, nums):
        i = 0

        while i < len(nums):
            correct = nums[i] - 1
            if 0 <= correct < len(nums) and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]

            else:
                i += 1
        
        missingNumbers = []
        for index in range(len(nums)):
            if nums[index] != index + 1:
                missingNumbers.append(index + 1)
         
        return missingNumbers
    

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [4, 3, 2, 7, 8, 2, 1, 5]  # Example input with some numbers missing
    result = solution.findDisappearedNumbers(nums)
    print("Missing numbers:", result)