# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # level order trerverse
        dq = deque()
        dq.append(root)
        sum = 0
        while(dq):
            node = dq.popleft()
            if low <= node.val <= high:
                sum += node.val
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        return sum
        