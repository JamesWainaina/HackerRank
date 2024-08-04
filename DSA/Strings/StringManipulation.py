#!/usr/bin/python3

"""
- A String  of >= 3 characters (all charaters will be digit characters. eg. '0 -9')
- There exists a partitioning of the string into substrings such that any 
 2 previous substrings sum to the value of the next substring in the partitioning.

Given a string s, determine whether s is an additive sequence.

Input s = '347111829'
Output: True

Input s = '15051101152'
Output: True

Input s = '15141161152'
Output: False
"""

def is_additive(s: str) -> bool:
    def is_valid(start: int, a: int, b: int) -> bool:
        # Base case
        # if start == len(s) then we have reached the end of the string
        if start == len(s):
            return True
        # Then we need to check if the sum of a and b is equal to the next
        sum_ab = str(a + b)
        # If the sum of a and b is not equal to the next substring in the partitioning
        if not s.startswith(sum_ab, start):
            return False
        # If the sum of a and b is equal to the next substring in the partitioning
        return is_valid(start + len(sum_ab), b, int(sum_ab))
    
    n = len(s)
    for i in range(1, n):
        for j in range(i + 1, n):
            a = int(s[:i])
            b = int(s[i:j])
            if is_valid(j, a, b):
                return True
    return False


print(is_additive('347111829')) # True
print(is_additive('15051101152')) # True
print(is_additive('15141161152')) # False