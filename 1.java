

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // map store target, value
        Map <Integer, Integer> map = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if (map.containsKey(target - nums[i])){
                int[] arr = {map.get(target-nums[i]),i};
                return arr;
            }
            else{
                map.put(nums[i],i);
            }

        }
        return null;
    }
}