#!/usr/bin/python3

"""The height of a binary search tree is the number of edges between the trees node and its
furthest leaf.You are given a pointer, node pointing to the root of the binary search tree.Complete 
the getHeight fuction provided in your editor so that it returns the height of the binary search tree.
"""

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
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
    def getHeight(self, root):
        if not root:
            return -1
        if not root.left and not root.right:
            return 0
        left_height = self.getHeight(root.left)
        rigth_height = self.getHeight(root.right)
        return max(left_height, rigth_height) + 1 # formular for getting the max height
    

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data=int(input())
    root=myTree.insert(root, data)
height= myTree.getHeight(root)
print(height)