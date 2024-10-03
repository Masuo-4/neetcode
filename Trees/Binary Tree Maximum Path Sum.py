# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(node):
            nonlocal res
            if not node: return 0
            leftmax = dfs(node.left)
            rightmax = dfs(node.right)
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            res = max(res, node.val + leftmax + rightmax)

            return node.val + max(leftmax, rightmax)

        dfs(root)
        return res
