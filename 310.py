# time: V + E
# space: V + E

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # create the graph
        if n == 1:
            return [0]
        graph = {}
        for edge in edges: 
            a = edge[0]
            b = edge[1]
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]

        # create indegree
        indegree = [0 for node in graph]
        order = []
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        
        vis = [0 for node in graph]
        # create queue
        dq = deque()
        for node in graph: 
            if indegree[node] == 1:
                dq.append(node)

        level = 0
        removed_count = 0
        while(n - removed_count > 2):
            removed_count += len(dq)
            level += 1
            for i in range(len(dq)): 
                node = dq.popleft()
                vis[node] = 1
                for neighbor in graph[node]:
                    if not vis[neighbor]:
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 1:
                            dq.append(neighbor)
        return list(dq)