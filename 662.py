# time: n
# space: m(node in a row)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # BT traversal
        queue = deque() # 直接在deque括号内写的collections会被分开成element存到queue中
        queue.append((root,0,0))
        bound = []
        max_bound = 1
        while queue:
            node, location, level = queue.popleft()
            if node is not None:
                if len(bound) == level:
                    bound.append([location,location])
                else:
                    bound[level][1] = location
                    max_bound = max(max_bound, bound[level][1] - bound[level][0] + 1)
                queue.append((node.left, location*2, level+1))
                queue.append((node.right, location*2 + 1, level+1))
        return max_bound