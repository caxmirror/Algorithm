# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            lenq = len(q)
            right = None
            for _ in range(lenq):
                cur = q.popleft()
                if cur:
                    right = cur
                    q.append(cur.left)
                    q.append(cur.right)
            if right:
                res.append(right.val)

        return res
                

         