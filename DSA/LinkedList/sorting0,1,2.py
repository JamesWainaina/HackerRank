#!/usr/bin/python3

"""
Given a linked list of N nodes where nodes can contain 
values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s 
linked list such that all zeros segregate to head side, 2s at the end of the linked list,
and 1s in the mid of 0s and 2s."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def segregate(self, head):
        self.head = head


        if self.head is None:
            return False
        
        zero_dummy = zero_tail = Node(None)
        one_dummy = one_tail = Node(None)
        two_dummy = two_tail = Node(None)

        current = head

        while current:
            if current.data == 0:
                zero_tail.next = current
                zero_tail = zero_tail.next
            elif current.data == 1:
                one_tail.next = current
                one_tail = one_tail.next
            else:
                two_tail.next = current
                two_tail = two_tail.next
            current = current.next
        
        zero_tail.next = one_dummy.next if one_dummy.next else two_dummy.next
        one_tail.next = two_dummy.next

        head = zero_dummy.next

        two_tail.next = None

        return head
    
    def printList(self, head):
        current = head
        while current:
            print(current.data, end="")
            current = current.next
        print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(0)

solution = Solution()
print("Original Linked List:")
solution.printList(head)

# Segregate the linked list

head = solution.segregate(head)

print("\nSegregated Linked List:")
solution.printList(head)