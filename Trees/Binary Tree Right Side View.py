# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        if root: q.append(root)
        while q:
            lenq = len(q)
            for _ in range(lenq):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(node.val)        
        return res

## LevelOrderでの回答をもとに、ループ終わりのnodeのみをリストに追加するようにした。
