# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            # ループ開始時にright_nodeを初期化する。
            right_node = None
            lenq = len(q)
            for i in range(lenq):
                node = q.popleft()
                if node:
                    right_node = node
                    q.append(node.left)
                    q.append(node.right)
            # 各階層のループが終わったとき、その時のright_nodeが本当のright_nodeなのでresに追加する。
            if right_node:
                res.append(right_node.val)
        return res
