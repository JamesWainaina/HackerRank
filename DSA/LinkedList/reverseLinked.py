#!/usr/bin/python3

"""reversing a linked list"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self, head):
        self.head = head
    
    def reverseLinkedList(self):
        if self.head is None:
            return None
        
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev  # Update the head of the linked list to the new head

    def printList(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

solution = Solution(head)
print("Original Linked List:")
solution.printList(head)

# Reverse the linked list
solution.reverseLinkedList()

print("\nReversed Linked List:")
solution.printList(solution.head)
