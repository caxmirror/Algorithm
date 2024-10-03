class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        dir = [[0,-1],[0,1],[1,0],[-1,0]]
        res = 0
        row = len(grid)
        col = len(grid[0])
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:
            lenq = len(q)
            for _ in range(lenq):
                i,j = q.popleft()
                for x,y in dir:
                    tmpi = i+x
                    tmpj = j+y
                    if 0<=tmpi<row and 0<=tmpj<col and grid[tmpi][tmpj] == 1:
                        grid[tmpi][tmpj] = 2
                        fresh -= 1
                        q.append((tmpi, tmpj))
            res += 1

        return res if fresh == 0 else -1
