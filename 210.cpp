// time: V + E
// space: V + E
// Khan做法, 很容易背板的
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        //graph 
        vector<vector<int>> g(numCourses);
        for(auto & p : prerequisites) {
            int a = p[0], b = p[1];
            g[b].push_back(a);
        }

        vector<int> indegree(numCourses), order;
        for (int i = 0; i < numCourses; i++) {
            for (int v : g[i]) {
                indegree[v]++;
            }
        }

        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        while(!q.empty()) {
            int node = q.front(); q.pop();
            order.push_back(node);
            for (int neighbor : g[node]) {
                indegree[neighbor]--;
                if(indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        return (order.size() == numCourses) ? order : vector<int>();
    }
};