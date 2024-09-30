# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root,0]]
        max_depth = 0

        while stack:
            root,depth = stack.pop()
            if root:
                stack.append([root.left,depth+1])
                stack.append([root.right,depth+1])
                max_depth = max(depth + 1, max_depth)
        return max_depth
        