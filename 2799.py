class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        total_d = len(set(nums))
        for i in range(len(nums)):
            cur_d = set()
            for j in range(i,len(nums)):
                cur_d.add(nums[j])
                if len(cur_d) == total_d:
                    res += 1
        return res
