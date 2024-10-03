# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]
        def dfs(root):
            if root == None:
                return 0
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)
            path = left + right + root.val
            res[0] = max(res[0], path)
            return max(left,right)+root.val
        dfs(root)
        return res[0]

