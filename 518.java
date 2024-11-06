//time: n * amount
//space: amount
public class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1; // Base case: one way to make amount 0
        
        // For each coin, update the dp array
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                System.out.println(Arrays.toString(dp));
                dp[i] += dp[i - coin];
            }
        }
        
        return dp[amount];
    }
}

