# time: n
# space: 1
class Solution_best:``
    def numTilings(self, n: int) -> int:
        mod = 1000000007
        dp = [0] * 4
        dp[3] = 1
        for i in range(1, n + 1):
            newdp = [0] * 4
            newdp[0] = (dp[1] + dp[2] + dp[3]) % mod
            newdp[1] = (dp[2] + dp[3]) % mod
            newdp[2] = (dp[1] + dp[3]) % mod
            newdp[3] = (dp[0] + dp[3]) % mod
            dp = newdp
        return dp[3]


# time: n
# space: n
class Solution_me:
    def numTilings(self, n: int) -> int:
        mod = 1000000007
        dp = [[0 for j in range(4)]for i in range(n+1)]
        dp[0][3] = 1
        for i in range(1, n + 1):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]) % mod
            dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % mod
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % mod
            dp[i][3] = (dp[i - 1][0] + dp[i - 1][3]) % mod
        return dp[n][3]
