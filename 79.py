# time: m*n*4^L
# space: L
class Solution_best:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(x, y, counter):
            # Base case: if the entire word is matched
            if counter == len(word):
                return True
            
            # Check bounds and character match
            if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != word[counter]:
                return False
            
            # Temporarily mark the cell as visited
            temp = board[x][y]
            board[x][y] = '#'

            # Explore all four directions
            found = (dfs(x + 1, y, counter + 1) or
                     dfs(x - 1, y, counter + 1) or
                     dfs(x, y + 1, counter + 1) or
                     dfs(x, y - 1, counter + 1))
            
            # Restore the cell's original value
            board[x][y] = temp
            
            return found

        # Start DFS from every cell that matches the first character of the word
        for m in range(rows):
            for n in range(cols):
                if board[m][n] == word[0] and dfs(m, n, 0):
                    return True
        
        return False



# time: m*n*4^L
# space: L
class Solution_me:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        # DFS - stack or recursive
        def dfs(x,y,path,counter): # do not use visited if path is more meaningful
            if counter == len(word):
                return True
            if 0 <= x < rows and 0 <= y < cols and (x,y) not in path and board[x][y] == word[counter]:
                path.add((x,y)) # 如何区分不同的path
                return dfs(x+1,y,path.copy(),counter+1) or dfs(x,y+1,path.copy(),counter+1) or dfs(x-1,y,path.copy(),counter+1) or dfs(x,y-1,path.copy(),counter+1) # return by multp
            else:
                return False
        for m in range(rows):
            for n in range(cols):
                if board[m][n] == word[0]:
                    path = set()
                    if dfs(m,n,path,0):
                        return True
        return False

