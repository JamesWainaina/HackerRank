#!/usr/bin/python3

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.findSquare(slow)  # Should use `slow` here
            fast = self.findSquare(self.findSquare(fast))  # Should use `fast` here

            if slow == fast:
                break
        return slow == 1
    
    def findSquare(self, n: int) -> int:
        ans = 0
        while n > 0:
            rem = n % 10
            ans += rem * rem
            n = n // 10
        return ans
    
if __name__ == "__main__":
    n = 19
    obj = Solution()
    print(obj.isHappy(n))
