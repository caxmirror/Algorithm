# time: n^2
# space: 1
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m = len() - 1
        # 0，0 -> 0, m
        # 0, 1 -> 1, m
        # 0, 2 -> 2, m
        # 1, 0 -> 0, m - 1
        # 2, 0 -> 0, m - 2
        # 3 - 9 - 8 - 2 2 + 0
        # 4 - 16 - 16 - 4 3 + 1
        # 5 - 25 - 24 - 6 4 + 2
        # 6 - 36 - 36 - 9 5+3+1 (1+5) * (len//2) / 2
        # 123456 5 + 3 + 1
        # 12345
        m = len(matrix) - 1
        
        for i in range(0, (m+1)//2):
            for j in range(i, m - i):
                x, y = i, j
                tmp1 = matrix[x][y]
                for k in range(4):
                    x_next = y
                    y_next = m - x
                    tmp2 = matrix[x_next][y_next]
                    matrix[x_next][y_next] = tmp1
                    tmp1 = tmp2
                    x = x_next
                    y = y_next