class Solution {
    public void moveZeroes(int[] nums) {
        int p0 = 0;
        int pn0 = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i]==0){p0=i; pn0=i+1;break;}
        }
        if (pn0 == 0){return;}
        while (pn0 < nums.length){
            if (nums[pn0] != 0){
                nums[p0] = nums[pn0];
                nums[pn0] = 0;
                p0 += 1;
                pn0 += 1;
            }
            else{pn0 += 1;}
        }
        return;
    }
}

class Solution1 {
    public void moveZeroes(int[] nums) {
        int l = 0;
        for (int r = 0; r < nums.length; r++){
            if (nums[r] != 0){
                int tmp = nums[r];
                nums[r] = 0;
                nums[l] = tmp;
                l += 1;
            }
        }
    }
}