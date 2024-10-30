class Solution {
    public int minMoves2(int[] nums) {
        // Not average, use median
        Arrays.sort(nums);
        int mid = nums.length/2;
        int tar = nums[mid];

        int res = 0;
        for (int num:nums){
            res += Math.abs(num - tar);  
        }
        return res;

    }
}