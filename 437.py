# Definition for a binary tree node.s
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root,d):
            if not root: 
                return 0
            else: 
                newd = {}
                res = 0
                newtar = targetSum - root.val
                if newtar == 0:
                    res += 1
                if newtar in d:
                    res += d[newtar]

                for k, v in d.items():
                    tmp = k + root.val
                    if tmp not in newd:
                        newd[tmp] = v
                    else: 
                        newd[tmp] += v
                if root.val not in newd:
                        newd[root.val] = 1
                else: 
                    newd[root.val] += 1

                return res + dfs(root.left,newd) + dfs(root.right,newd)
        return dfs(root,{})

