//time: n * target
//space: target
class Solution {
    public boolean canPartition(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        // If total sum is odd, it's not possible to partition it equally.
        if (totalSum % 2 != 0) return false;

        int target = totalSum / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;  // Base case: A sum of 0 is always possible.

        // Iterate through each number in the array.
        for (int num : nums) {
            // Traverse backwards to avoid overwriting values needed for this iteration.
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }

        return dp[target];
    }
}



// time: n * 2^n
// space: 2^n
class Solution_me_bad {
    public boolean canPartition(int[] nums) {
        int tar = 0;
        for (int num:nums){
            tar += num;
        }
        if(tar%2==1){return false;}
        tar /= 2;
        Set<Integer> set = new HashSet<>();
        for (int num: nums){
            Set<Integer> tmpset = new HashSet<>(set); // set travesal modification
            tmpset.add(tar - num);
            for (int num2: set){
                int remain = num2 - num;
                if (remain == 0||num2 == 0){return true;}
                tmpset.add(num2 - num);
            }
            set = tmpset;
        }
        return false;
    }
}

