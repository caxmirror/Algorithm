// time: n * sum(abs(nums))
// space: sum(abs(nums))
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = 0;
        for (int num : nums) sum += num;

        // If (target + sum) is odd or less than 0, no valid partition.
        if ((target + sum) % 2 != 0 || target > sum) return 0;

        int subsetSum = (target + sum) / 2;

        return countSubsetsWithSum(nums, subsetSum);
    }

    private int countSubsetsWithSum(int[] nums, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1;  // One way to make sum 0 (by not choosing any element).

        for (int num : nums) {
            for (int j = target; j >= num; j--) {
                dp[j] += dp[j - num];
            }
        }
        return dp[target];
    }
}


// time: n * sum(abs(nums))
// space: sum(abs(nums))
class Solution_me {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = 0;
        for(int num:nums){
            sum += Math.abs(num);
        }
        int [] dp = new int[sum*2 + 1];
        dp[sum + nums[0]] += 1;
        dp[sum - nums[0]] += 1;
        // 0 + sum -> real 0
        for(int j = 1; j < nums.length; ++j){
            int num = nums[j];
            //System.out.println(Arrays.toString(dp));
            int [] newdp = new int[sum*2 + 1];
            for(int i=0;i< dp.length;++i){
                if(i-Math.abs(num) >= 0){newdp[i] += dp[i-Math.abs(num)];} // arr defalut value
                if(i+Math.abs(num) < dp.length){newdp[i] += dp[i+Math.abs(num)];}
            }
            dp = newdp;
        }
        return (Math.abs(target) > sum) ? 0 : dp[sum + target];
    }
}