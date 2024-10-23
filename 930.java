class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        return helper(nums,goal) - helper(nums,goal - 1);
    }

    public int helper(int[] nums, int goal){
        if (goal < 0) {return 0;}
        int l = 0;
        int res = 0;
        int cursum = 0;
        for (int r=0;r<nums.length;r++){
            cursum += nums[r]; 
            while (cursum > goal){ 
                cursum -= nums[l]; 
                l += 1; 
            } 
            res += (r - l + 1); 
        } 
        return res; 
    }
} 