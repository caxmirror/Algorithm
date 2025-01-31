# time : n
# space: 1
class Solution_best_me:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        cur_sum = 0
        max_sum = float("-inf")
        for right in range(len(nums)):
            cur_sum += nums[right]
            max_sum = max(max_sum, cur_sum)
            while cur_sum < 0 and left <= right:
                cur_sum -= nums[left]
                left += 1
        return max_sum
            