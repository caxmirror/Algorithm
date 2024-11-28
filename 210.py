# time: V + E
# space: V + E
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)} 
        indegree = {i:0 for i in range(numCourses)} 
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
        
        queue = deque([node for node in indegree if indegree[node] == 0])
        topo_loop = []

        while queue: 
            node = queue.popleft()
            topo_loop.append(node)
            for neighbour in graph[node]: 
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(topo_loop) == numCourses:
            return topo_loop
        else:
            return []
