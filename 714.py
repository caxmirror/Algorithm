from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0] 
        for i in range(len(prices)):
            cash = max(cash, prices[i] + hold - fee)
            hold = max(hold, cash - prices[i])
        return cash
