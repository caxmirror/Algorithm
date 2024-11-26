# time: n
# space: n
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        res = 0
        dic = {}
        for i in range(0, n + 1):
            if prefix_sum[i] - k in dic:
                res += dic[prefix_sum[i] - k]

            if prefix_sum[i] not in dic:
                dic[prefix_sum[i]] = 1
            else: 
                dic[prefix_sum[i]] += 1
        return res
