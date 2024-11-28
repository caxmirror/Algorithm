# time: n
# space: 1
class Solution_best:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current = root
        
        while current:
            if current.left:
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                predecessor.right = current.right
            
                current.right = current.left
                current.left = None
            current = current.right
            
