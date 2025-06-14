class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        # sliding window
        left = 0
        for right in range(1, len(nums)):
            if nums[right] <= nums[right - 1]:
                left = right
            res = max(res, right - left + 1)
        return res
