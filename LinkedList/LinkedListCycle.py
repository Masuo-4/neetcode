# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        node = head
        while node:
            if node in node_set:
                return True
            node_set.add(node)
            node = node.next
        return False
