# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# time: logn
# space: 1
class Solution_me_best:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            
            mid = (left + right) // 2
            
            if not isBadVersion(mid):
                left = mid + 1
            else:
                if mid == 1 or not isBadVersion(mid - 1):
                    return mid
                else: 
                    right = mid - 1
        return -1
            