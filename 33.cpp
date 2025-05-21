class Solution_best_me {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = (int)nums.size() - 1;
        while (l <= r){
            printf("l = %d, r = %d\n", l, r);
        int mid = l + (r - l) / 2;
        if (nums[mid] == target) {return mid;}
        if (nums[l] < nums[r]) 
        {
            nums[mid] > target ? r = mid - 1 : l = mid + 1;
        }
        else
        {
            if (nums[mid] >= nums[l]) {
                if (target > nums[mid]) {
                    l = mid + 1;
                }
                else {
                    if (target >= nums[l]){
                        r = mid - 1;
                    }
                    else {
                        l = mid + 1;
                    }
                }
            }
            else {
                if (target < nums[mid]) {
                    r = mid - 1;
                }
                else {
                    if (target >= nums[l]){
                        r = mid - 1;
                    }
                    else {
                        l = mid + 1;
                    }
                }
            }
        }
        }
        return -1;
    }
};