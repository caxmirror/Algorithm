class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(len(word1)-1, -1, -1):
            dp[i][len(word2)] = dp[i+1][len(word2)] + 1 
        for j in range(len(word2)-1, -1, -1):
            dp[len(word1)][j] = dp[len(word1)][j+1] + 1

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j+1],dp[i+1][j],dp[i][j+1])+1
        return dp[0][0]