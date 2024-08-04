#!/usr/bin/python3
class Node:
	def __init__(self, data):
		self.next = None
		self.data = data 
class Solution:
	def insert(self, head, data):
		p = Node(data)
		if head == None:
			head = p
		elif head.next == None:
			head.next = p
		else:
			start = head
			while (start.next!= None):
				start = start.next
			start.next = p
		return head
	def display(self,head):
		current = head
		while current:
			print(current.data, end="")
			current = current.next
	def removeDuplicates(self,head):
		if not head:
			return None
		current = head
		while current.next:
			if current.next.data == current.data: # point to the next node 
				current.next = current.next.next
			else:
				current = current.next
		return head


T = int(input())
mylist= Solution()
head = None
for i in range(T):
	data = int(input())
	head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head) 

