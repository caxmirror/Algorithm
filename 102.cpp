/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        // 1.queue
        // 2.count to access current level -> no need to store extra things
        queue<TreeNode *> q;
        if (root != nullptr) {
            q.push(root);
        }
        vector<vector<int>> result;

        while (!q.empty()) {
            vector<int> curr;
            curr.reserve(q.size()); // reserve for vector and string

            int count = (int)q.size();
            while(count-- > 0) {
                TreeNode* node = q.front(); q.pop();
                curr.push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            result.push_back(move(curr)); 
        }
        return result;
    }
};

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        // 1.deque to store curr pointer
        // 2.use
        deque<pair<TreeNode *, int>> dq;
        dq.push_back({root, 0});
        vector<vector<int>> result;
        int cur_level = -1;
        while (!dq.empty()) {
            auto [node, level] = dq.front(); dq.pop_front();
            if (node != nullptr) {
                if (level > cur_level) {
                    result.push_back({});
                    cur_level += 1;
                }
                result.back().push_back(node->val);
                dq.push_back({node->left, level + 1});
                dq.push_back({node->right, level + 1});
            }
        }
        return result;
    }
};