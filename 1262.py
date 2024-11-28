# time: n
# space: 1
class Solution_best:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            current_dp = dp[:]
            for i in range(3):
                new_sum = current_dp[i] + num #
                if new_sum != float('-inf'):
                    dp[new_sum % 3] = max(dp[new_sum % 3], new_sum)
        return dp[0]