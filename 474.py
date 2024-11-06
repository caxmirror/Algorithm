def findMaxForm(strs, m, n):
    # Initialize the DP array with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Iterate over each string in strs
    for s in strs:
        # Count the number of 0's and 1's in the current string
        count_zeros = s.count('0')
        count_ones = s.count('1')
        
        # Update the DP array in reverse to prevent counting a string multiple times
        for i in range(m, count_zeros - 1, -1):
            for j in range(n, count_ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - count_zeros][j - count_ones] + 1)

    # The result is stored in dp[m][n]
    return dp[m][n]
