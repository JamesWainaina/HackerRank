#!/usr/bin/python3


class FindAllduplicates(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0

        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i] , nums[correct] = nums[correct] , nums[i]
            else:
                i += 1
        
        duplicate_numbers = []
        for index in range(len(nums)):
            if nums[index] != index + 1:
                duplicate_numbers.append(nums[index])
        return duplicate_numbers

if __name__ == "__main__": 
    solution = FindAllduplicates()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]  # Example input with some numbers missing
    result = solution.findDuplicates(nums)
    print("Duplicate numbers:", result)