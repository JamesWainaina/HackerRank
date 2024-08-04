#!/usr/bin/python3

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    
    def calculateCycleLength(self, head: Optional[ListNode]) -> int:
        slow = head 
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                temp =slow
                length = 0
                while True:
                    temp = temp.next
                    length += 1
                    if temp == slow:
                        break
                return length
        return 0

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Creates a cycle

# Test
solution = Solution()
print(solution.hasCycle(node1)) 


# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Test
solution = Solution()
print(solution.hasCycle(node1))  # Expected output: False
