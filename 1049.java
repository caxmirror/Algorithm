//time: n * sum
//space: sum
class Solution {
    public int lastStoneWeightII(int[] stones) {
        int totalSum = 0;
        for (int stone : stones) totalSum += stone;

        int target = totalSum / 2;
        int[] dp = new int[target + 1];

        for (int stone : stones) {
            for (int j = target; j >= stone; j--) {
                dp[j] = Math.max(dp[j], dp[j - stone] + stone);
            }
        }
        return totalSum - 2 * dp[target];
    }
}
