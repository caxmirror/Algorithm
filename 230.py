# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_best:
    def kthSmallest(self, root, k):
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            cur = node.right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_me_worst:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        
        def dfs(node):
            nonlocal k, res
            if not node:
                return
            dfs(node.left)
            k -= 1
            if not k:
                res = node.val
            dfs(node.right)
        dfs(root)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_me_better:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def dfs(node):
            nonlocal k, res
            if not node:
                return
            dfs(node.left)
            k -= 1
            if k <= 0: # 剪枝，不执行后续内容
                if k == 0:
                    res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res