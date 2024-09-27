# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        cur = root
        while cur or stack:
            # cur != None, go to the very left
            while cur:
                stack.append(cur)
                cur = cur.left

            # cur == None, pop stack, add value, turn to right
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res  

        