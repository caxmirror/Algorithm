# time: m * n
# space: m * n
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row_bound = [0, len(matrix)-1]
        col_bound = [0, len(matrix[0])-1]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # traverse using visited
        i, j = 0, 0 
        dir = 0
        for count in range(len(matrix) * len(matrix[0])): 
            res.append(matrix[i][j])
            di = i + dirs[dir][0]
            dj = j + dirs[dir][1]
            if di > row_bound[1] or di < row_bound[0] or dj > col_bound[1] or dj < col_bound[0]:
                if di > row_bound[1]:
                    col_bound[1] -= 1
                elif di < row_bound[0]:
                    col_bound[0] += 1
                elif dj > col_bound[1]:
                    row_bound[0] += 1
                else:
                    row_bound[1] -= 1
                dir = (dir + 1) % 4
                i += dirs[dir][0]
                j += dirs[dir][1]
            else: 
                i, j = di, dj
        return res
            


