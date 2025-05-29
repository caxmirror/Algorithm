class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        int n = (int)nums.size();
        for (int i = 0; i < (int)nums.size() - 2; i++) {
            int j = i + 1, k = n - 1;
            while(j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    vector<int> new_result = {nums[i], nums[j], nums[k]};
                    result.push_back(new_result);
                    j += 1;
                    k -= 1;
                    while (j < n && nums[j] == nums[j - 1]) {
                        j += 1;
                    }
                    while (k > j && nums[k] == nums[k + 1]) {
                        k -= 1;
                    }
                } else if (sum > 0) {
                    k -= 1;
                } else {
                    j += 1;
                }
            }
            while (i < n - 2 && nums[i] == nums[i + 1]) {
                i += 1;
            }
        }
        return result;
    }
};