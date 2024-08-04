#!/usr/bin/python3

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def getMiddle(self, head):
        self.head = head

        if self.head is None:
            return False
        
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        current = head
        for i in range(count // 2):
            current = current.next
        return current.data
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Find the middle element of the linked list
solution = Solution()
middle_element = solution.getMiddle(head)
print("Middle element of the linked list:", middle_element)
    

