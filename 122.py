# time: n
# space: 1
class Solution_best_me:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit += prices[right] - prices[left]
                left = right
            if prices[right] < prices[left]:
                left = right
            right += 1
        return profit
