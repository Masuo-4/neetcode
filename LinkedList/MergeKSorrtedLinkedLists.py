# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merge_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merge_list.append(self.mergeLists(l1, l2))
            lists = merge_list
        return lists[0]
            
        


    def mergeLists(self, list1, list2):
        dummy = node = ListNode()
        A, B = list1, list2
        while A and B:
            if A.val > B.val:
                node.next = B
                B = B.next
            else:
                node.next = A
                A = A.next
            node = node.next
        if A:
            node.next = A
        if B:
            node.next = B
        return dummy.next
