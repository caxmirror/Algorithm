# time: N
# space: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = [root]
        def dfs(node):
            if node == None:
                return False
            left_return = dfs(node.left)
            right_return = dfs(node.right)
            if (node == p or node == q) and (left_return or right_return) or (left_return and right_return):
                result[0] = node
                return False
            if node == p or node == q:
                return True
            return left_return or right_return
        dfs(root)
        return result[0]
        