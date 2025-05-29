//stack not able to access the bottom, deprecate.
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = (int)nums.size();
        vector<int> ans((n - k + 1), 0);
        // monotonic stack
        deque<int> monotonic_stack;
        for (int i = 0; i < n; i++) {
            while (!monotonic_stack.empty() && monotonic_stack.front() < i - k + 1) {
                monotonic_stack.pop_front();
            }
            while (!monotonic_stack.empty() && (nums[monotonic_stack.back()] < nums[i])) {
                monotonic_stack.pop_back();
            }
            monotonic_stack.push_back(i);
            if (i >= k - 1) {
                ans[i - k + 1] = nums[monotonic_stack.front()];
            }
        }
        return ans;
    }
};