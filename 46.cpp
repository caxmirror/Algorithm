// time: n * n!
// space: n!
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        //backtracking
        vector<vector<int>> res;
        vector<int> path;
        vector<int> vis(nums.size());
        dfs(nums, vis, path, res);
        return res;
    }
    void dfs(vector<int>& nums, vector<int>& vis, vector<int>& path, vector<vector<int>>& res) {
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < (int)nums.size(); ++i) { //到底有没有必要写int?
            if (vis[i] == 0) {
                vis[i] = 1;
                path.push_back(nums[i]);
                dfs(nums, vis, path, res);
                vis[i] = 0;
                path.pop_back();
            }
        }
        return;
    }
};