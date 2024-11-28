# time: n
# space: n
class Solution_best:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        coverage = [0] * (n + 1)

        for l, r in queries:
            coverage[l] += 1
            if r + 1 < n:
                coverage[r + 1] -= 1

        for i in range(1, n):
            coverage[i] += coverage[i - 1]

        for i in range(n):
            if nums[i] > coverage[i]:
                return False

        return True