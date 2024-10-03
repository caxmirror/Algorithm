class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # sum and prefix
        prefix = {i:0 for i in range(k)}
        prefix[0] = 1
        total = 0
        res = 0
        for num in nums:
            total += num
            total = total%k
            res += prefix[total]
            prefix[total] += 1
        return res