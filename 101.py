# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left,right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                if left.val == right.val:
                    return dfs(left.left,right.right) and dfs(right.left,left.right)
                else:
                    return False
        return dfs(root.left,root.right)
