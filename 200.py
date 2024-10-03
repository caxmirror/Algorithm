class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visit = [[0 for j in range(col)]for i in range(row)]
        res = 0
        dir = [[0,1],[1,0],[-1,0],[0,-1]]

        def bfs(i,j):
            q = collections.deque()
            q.append((i,j))
            while q:
                i,j = q.popleft()
                for x,y in dir:
                    tmpi = i + x
                    tmpj = j + y
                    if 0 <= tmpi < row and 0 <= tmpj < col and grid[tmpi][tmpj] == "1" and visit[tmpi][tmpj] == 0:
                        visit[tmpi][tmpj] = 1
                        q.append((tmpi,tmpj))
                        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and visit[i][j] == 0:
                    visit[i][j] = 1
                    res += 1
                    bfs(i,j)
        return res
                    