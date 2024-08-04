#!/usr/bin/python3

class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next
class LinkedList:
	def __init__(self):
		self.head = None
	def insert_at_beginning(self, data):
		node = Node(data, self.head)
		self.head = node
	def print(self):
		if self.head is None:
			print("linked list is empty")
			return
		itr = self.head
		llstr = ''
		while(itr):
			itr = itr.next
