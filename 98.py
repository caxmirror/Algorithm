# time: n
# space: h
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float("-inf")

        def dfs(node):
            nonlocal prev
            if not node:
                return True
            left = dfs(node.left)
            if node.val <= prev:
                return False
            prev = node.val
            right = dfs(node.right)
            return left and right

        return dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node,left,right):
            if not node:
                return True
            if node.val > left and node.val < right:
                return valid(node.left,left,node.val) and valid(node.right,node.val,right)
            else:
                return False
        return valid(root,float("-inf"),float("inf"))
