# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, max_val):
            nonlocal count
            if not root: return 0
            if root.val >= max_val:
                count += 1
                max_val = root.val
            dfs(root.left, max_val)
            dfs(root.right, max_val)
            return count      
        return dfs(root, root.val)
 
 ############################
 
 #nonlocalを使わない別解↓↓↓
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_v):
            if not node: return 0
            if node.val >= max_v:
                res = 1
            else: res = 0
            max_v = max(max_v, node.val)
            res += dfs(node.left, max_v)
            res += dfs(node.right, max_v)
            return res

        return dfs(root, root.val)
