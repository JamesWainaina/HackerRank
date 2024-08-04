#!/usr/bin/python3

"""Given a singly linked list of size N. 
The task is to left-shift the linked list by k nodes, 
where k is a given positive integer smaller than or equal to length of the linked list."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        
        if not head or k == 0: # checks if the head is None or if K is 0 there is no need to rotate the list
            return head
            
        length = 1 # initializes the length to 1 counting form the head
        current = head
        
        while current.next: 
            length += 1 # when moving to the next node increment the node by one
            current = current.next # moving current to the next node until it reaches the end of the list
        
        k = k % length # Ensures the k is within to range of the list length.
        
        if k == 0: # if k i s 0 after the modulo operation,return head
            return head
        
        new_head_index = length - k # calculates the index of the new head after rotation and initializes variables for tracking previous and current nodes during traversal
        prev = None
        current = head

        for i in range(new_head_index): # This loop moves prev and current pointers to the nodes just before the new head. It repeats new_head_index times.
            prev = current
            current = current.next


        prev.next = None # This breaks the list connection by setting the next pointer of the previous node to None and assigns new_head to the current node, which becomes the new head after rotation.
        new_head = current
        
        
        while current.next: # This loop traverses the list until current reaches the last node.
            current = current.next
        
        current.next = head # This reconnects the last node of the rotated list to the original head, creating a circular structure.
        return new_head
    
    def printLinkedList(self, head):
        current = head
        while current:
            print(current.data, end="")
            current = current.next
        print()  # Add a new line after printing the linked list
    
    def left_shift(self, head, k):
        return self.rotate(head, k)

# Create an instance of the Solution class
solution = Solution()

# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original linked list:")
solution.printLinkedList(head)

k = 2
new_head = solution.left_shift(head, k)

print(f"After left-shifting by {k} nodes:")
solution.printLinkedList(new_head)
