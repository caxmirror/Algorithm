class Solution_outofmemory:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # 1.change to sliding window
        sorted_coins = sorted(coins)
        lbound = sorted_coins[0][0]
        rbound = sorted_coins[len(coins) - 1][1]
        dp = [0 for i in range(rbound - lbound + 1)]
        for coin in coins:
            for i in range(coin[0]-lbound, coin[1]-lbound + 1):
                dp[i] = coin[2]
                #dp[coin[0]-lbound:coin[1]-lbound + 1] = coin[2]
        left, right = 0, k
        if k >= len(dp):
            return sum(dp)
        sum_coins = sum(dp[0:k])
        max_coins = sum_coins
        while right < len(dp):
            sum_coins += dp[right] - dp[left]
            max_coins = max(max_coins, sum_coins)
            right += 1
            left += 1
        return max_coins

            



