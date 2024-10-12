class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        if target < matrix[0][0]:
            return False
        while l <= r:
            m = (l+r)//2
            print(m)
            if matrix[m][0] <= target:
                if m==len(matrix)-1 or matrix[m+1][0]>target:
                    l, r =0, len(matrix[0])-1
                    while l <= r:
                        mid = (l+r)//2
                        print(l,r,mid)
                        if matrix[m][mid] == target:
                            return True
                        elif matrix[m][mid] > target:
                            r = mid - 1
                        else:
                            l = mid + 1
                    return False
                else:
                    l = m + 1
            else: 
                r = m - 1
