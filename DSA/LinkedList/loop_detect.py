#!/usr/bin/python3

"""
Given a linked list of N nodes. 
The task is to check if the linked list has a loop.
Linked list can contain self loop."""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def detectLoop(self, head):
        self.head = head

        if self.head is None:
            return False
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = self.head.next
            fast_ptr = self.head.next.next
            if slow_ptr == fast_ptr:
                return True
        return False
    

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(4)
head.next.next.next = head.next
solution = Solution()
has_loop = solution.detectLoop(head)
if has_loop:
    print("The Linked list contains a loop")
else:
    print("The linked list does not contain a loop")