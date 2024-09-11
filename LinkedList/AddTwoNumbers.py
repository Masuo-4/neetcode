# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        kuriagari = 0
        dummy = node = ListNode()
        while l1 or l2 or kuriagari:
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0

            val = l1_num + l2_num + kuriagari
            kuriagari = val // 10
            node.next = ListNode(val % 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node = node.next

        return dummy.next
