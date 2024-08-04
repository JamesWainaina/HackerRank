from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start = self.search(nums, target, True)
        end = self.search(nums, target, False)
        return [start, end]

    def search(self, nums, target, findStartIndex):
        ans = -1
        start = 0
        end = len(nums) - 1 

        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid
                if (findStartIndex):
                    end = mid - 1
                else:
                    start = mid + 1
        return ans

solution = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(solution.searchRange(nums, target)) 