# time: V + E
# space: V + E
from collections import deque
class Solution_best_me:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph
        # indegree
        graph = {i: [] for i in range(numCourses)} # remember
        indegree = {i: 0 for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            indegree[course] += 1
            graph[prerequisite].append(course)
        
        queue = deque(node for node in graph if indegree[node] == 0)
        topo_path = []
        while queue:
            node = queue.popleft()
            topo_path.append(node)
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(topo_path) == numCourses: 
            return True
        else: 
            return False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)} # 1.initialize dict
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            pres = preMap[crs]
            visit.add(crs)
            for pre in pres: 
                if not dfs(pre): #2.return backtracking return value is important
                    return False
            preMap[crs] = []
            visit.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
