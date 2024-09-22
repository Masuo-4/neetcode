# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = node = ListNode(0, head)
        # gfnを見つける
        while True:
            gfn = self.findFinalNode(node, k)
            if not gfn:
                break    
                
            gnn = gfn.next
            nxt = gnn
            curr = node.next
            while curr != gnn:
                temp = curr.next
                curr.next = nxt
                nxt = curr
                curr = temp
            
            temp = node.next
            node.next = nxt
            node = temp
        
        return dummy.next


    def findFinalNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
