# time: m*n
# space: m*n
class Solution_me:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set() # visited for each dfs, clear each time
        edge_island = set() # not edge
        not_edge_island = set()

        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        flag = 0                
        def dfs(i, j):
            nonlocal flag
            visited.add((i,j))
            for di, dj in dirs:
                if 0 <= (i + di) < len(board) and 0 <= (j + dj) < len(board[0]) and board[i + di][j + dj] == "O" and (i + di, j + dj) not in visited:
                    dfs(i + di, j + dj)
            if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                flag = 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if (i,j) in edge_island:
                        continue
                    elif (i,j) in not_edge_island:
                        board[i][j] = "X"
                    else: 
                        dfs(i, j) # edge
                        if flag == 1:
                            edge_island = visited | edge_island
                            flag = 0
                        else: 
                            board[i][j] = "X"
                            not_edge_island = visited | not_edge_island
                        visited = set()
