// time: n
// space: 1

class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        // sliding window
        int left = 0;
        int res = nums.length + 1;
        int cur_sum = 0;
        for (int right = 0; right < nums.length; right++) {
            cur_sum += nums[right];
            while (cur_sum >= target) {
                res = Math.min(res, right - left + 1);
                cur_sum -= nums[left];
                left += 1;
            }
        }
        return res ==  nums.length + 1 ? 0 : res;
    }
}