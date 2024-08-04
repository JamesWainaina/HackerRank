#!/usr/bin/python3
"""
Given two singly linked lists of size N and M, 
write a program to get the point where two linked lists intersect each other.
"""

# O(N + M) which is the length of both n and m

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_length(head):
    res = 0
    while head:
        head = head.next
        res += 1
    return res

def intersection(head1 , head2):
    n1 = get_length(head1)

    n2 = get_length(head2)

    while n1 > n2:
        head1 = head1.next
        res -= 1
    while n2 > n1:
        head2 = head2.next
        res -= 1
    
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next
    
    if head1 is not None:
        return head1.data
    return -1

     
