#!/usr/bin/python3

"""
A Node class has an integer data field, data, and a Node instance provider, next, 
pointing to another node.(ie the next node in a list).

A Node insert function is also declared in your editor it has two parameters, a pointer, 
head pointing pointing to the first node of a linked list, and an integer data value that must
be added to the end of the lsit as a new Node object.

Task:
Complete the insert fuction in your editor so that it creates a new node (pass data as the Node 
constructor argument() and inserts it to the tail of the linked list referenced by the head parameter.
Once the new node is added, return the reference to the head node.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        if not head:
            return new_node
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head



mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

mylist.display(head)
        