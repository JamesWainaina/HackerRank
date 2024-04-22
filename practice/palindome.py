#!/usr/bin/python3

"""A palidrome is a word, phrase, number, or other sequence of characters which reads the 
same backwords and forwards. can you determine if a given phrase is a palindrome.

write the following:
1. Two instance variables, one of your stack and queue.
2. A void pushCharacter(char ch) method that pushes a charcter onto a stack.
3. A void enqueuCharcater(char ch) method that enqueus a character in the queue instance variable.
4. A char popCharacter method that pops and returns the character at the top of the stack instance variable
5. A char dequeuCharacter() method that dequeues and returns the first character in the queue instance variable
"""
import sys
from collections import deque

class Solution:
    def __init__(self):
        self.stack = list()
        self.queue = deque()

    def pushCharacter(self, character):
        self.stack.append(character)

    def enqueueCharacter(self, character):
        self.queue.append(character)

    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        return self.queue.popleft()

s = input()

obj = Solution()

l = len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
isPalindrome = True

"""Pop the top character from the stack
dequeue the first character from queue
compare both chcaracters"""

for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
if isPalindrome:
    print(f"The word, {s}, is palindrome".format(s))
else:
    print(f"The word, {s}, is not a palindrome".format(s))
