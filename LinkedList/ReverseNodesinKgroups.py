# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = node = ListNode(0, head) 
        while True:
            group_final_node = self.get_final_node(node, k)
            if not group_final_node:
                break
            group_next_node = group_final_node.next
            prev = group_next_node  # 次に接続すべきノード（グループの逆の方向）
            curr = node.next  # 現在処理しているグループの最初のノード
            while curr != group_next_node:
                tmp = curr.next
                curr.next = prev  # 今処理しているノードのnextを逆転
                prev = curr  # prevを現在のノードに更新
                curr = tmp  # currを次のノードに更新
            
            # グループの前の部分を逆転された部分に接続
            tmp = node.next
            node.next = prev  # 逆転されたグループの先頭に接続
            node = tmp  # 次のグループの先頭に移動

        return dummy.next

    def get_final_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
