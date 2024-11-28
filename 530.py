# time: n
# space: h, (call stack: h, memory: 1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# preorder
class Solution_best_me:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        prev = float("inf")

        def dfs(node):
            nonlocal prev, res
            if not node:
                return
            dfs(node.left)
            res = min(res, abs(node.val - prev))
            prev = node.val
            dfs(node.right)

        dfs(root)
        return res
