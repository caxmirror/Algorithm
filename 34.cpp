class Solution_best_me {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = 0, r = (int)nums.size() - 1;
        // find left
        int left = -1;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > target) {r = mid - 1;}
            else if (nums[mid] < target) {l = mid + 1;}
            else {
                if (mid == 0 or nums[mid - 1] < target){
                    left = mid;
                    break;
                }
                else {
                    r = mid - 1;
                }
            }
        }
        // find right
        l = 0, r = (int)nums.size() - 1;
        int right = -1;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > target) {r = mid - 1;}
            else if (nums[mid] < target) {l = mid + 1;}
            else {
                if (mid == (int)nums.size() - 1 or nums[mid + 1] > target){
                    right = mid;
                    break;
                }
                else {
                    l = mid + 1;
                }
            }
        }
        return {left, right};
    }
};