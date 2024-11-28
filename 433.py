# time: 
# space: 
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # deque
        dirs = ["A","C","G","T"]

        def graph(node):
            neighbours = []
            for i in range(len(node)):
                for di in dirs:
                    neighbours.append(node[:i] + di + node[i+1:])
            return neighbours

        def is_valid(node):
            if node in bank:
                return True
            else:
                return False
        
        visited = set(startGene)
        queue = deque()
        queue.append((startGene, 0))
        while queue:
            node, k = queue.popleft()
            if node == endGene:
                return k
            for neighbour in graph(node):
                if is_valid(neighbour) and neighbour not in visited:
                    queue.append((neighbour, k+1))
                    visited.add(neighbour)
        return -1

                
