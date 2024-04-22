#!/usr/bin/python3

"""A level-order traversal also known as breadth-first search, values each level of a tree's nodes
from left to right, to the bottom.You are given a pointer, root, pointing to the root of the 
binary-search tree.Complete the levelOrder function provided in your editor so that it prints the 
level-order traversal of the binary search tree."""

# we use queus FIFO

import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Solution:
    def insert(self, root , data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root
        
    def levelOrder(self, root):
        nodes_to_search = list() # because we can insert and pop at the end of a list
        nodes_travesed = '' # keep a record of nodes traversed
        nodes_to_search.append(root)
        while len(nodes_to_search) > 0:
            node = nodes_to_search.pop(0)
            if node.left:
                nodes_to_search.append(node.left)
            if node.right:
                nodes_to_search.append(node.right)
            nodes_travesed +=  str(node.data) + ' '
        print(nodes_travesed)

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)

    