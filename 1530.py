# time: n^2
# space: n

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_me_best: 
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        res = [0]
        def backtrack(node):
            if node == None:
                return []
            if node.left == None and node.right == None:
                return [0]
            
            left_leafs = [k + 1 for k in backtrack(node.left) if k < distance - 1]
            right_leafs = [k + 1 for k in backtrack(node.right) if k < distance - 1]
            for right_leaf in right_leafs:
                for left_leaf in left_leafs:
                    if right_leaf + left_leaf <= distance:
                        res[0] += 1
            return left_leafs + right_leafs

        backtrack(root)
        return res[0]
    

# time: n^2 -> n^2 comparison
# space: n

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_me: 
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        res = [0]
        def backtrack(node):
            if node.left == None and node.right == None:
                return [0]
            elif node.left == None and node.right != None:
                return [k + 1 for k in backtrack(node.right)]
            elif node.left != None and node.right == None:
                return [k + 1 for k in backtrack(node.left)]
            else: 
                left_leafs = [k + 1 for k in backtrack(node.left)]
                right_leafs = [k + 1 for k in backtrack(node.right)]
                for right_leaf in right_leafs:
                    for left_leaf in left_leafs:
                        if right_leaf + left_leaf <= distance:
                            res[0] += 1
                left_leafs.extend(right_leafs)
                return left_leafs
        backtrack(root)
        return res[0]