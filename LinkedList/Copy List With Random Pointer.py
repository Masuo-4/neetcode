"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_copy = {None: None}
        old = head
        while old:
            old_copy[old] = Node(old.val)
            old = old.next

        old = head
        while old:
            old_copy[old].next = old_copy[old.next]
            old_copy[old].random = old_copy[old.random]
            old = old.next
        return old_copy[head]
