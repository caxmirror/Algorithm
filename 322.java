//time: n * amount
//space: amount
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);  // Initialize with a value larger than amount.
        dp[0] = 0;  // Base case: 0 coins to make amount 0.

        for (int coin : coins) {
            for (int j = coin; j <= amount; j++) {
                dp[j] = Math.min(dp[j], dp[j - coin] + 1);
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
}

//time: n * amount
//space: amount
class Solution_me {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0){return 0;}
        Arrays.sort(coins);
        int [] dp = new int [amount+1];
        for (int i = coins.length-1; i >= 0; --i){
            for(int j=coins[i]; j <= amount; j += 1){
                if (dp[j-coins[i]]!=0 || j-coins[i] == 0){
                    dp[j] = (dp[j]==0) ? dp[j-coins[i]] + 1 : Math.min(dp[j], dp[j-coins[i]] + 1);
                }
            }
        }
        return dp[amount] != 0 ? dp[amount] : -1 ;
    }
}
