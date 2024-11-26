# time: n
# space: n
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)

        for i in range(0,len(nums)):
            nums[i] = -1 if nums[i] == 0 else 1

        prefix_sum[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        dic = {0: -1}
        max_res = 0
        for i in range(len(nums)):
            if prefix_sum[i] not in dic:
                dic[prefix_sum[i]] = i
            else: 
                max_res = max(max_res, i - dic[prefix_sum[i]])
        return max_res
