//no need to use visit, more efficient!
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = (int)grid.size(), cols = (int)grid[0].size();
        int ans = 0;
        for (int x = 0; x < rows; ++x) {
            for (int y = 0; y < cols; ++y) {
                if (grid[x][y] == '1') {
                    ans += 1;
                    dfs(x, y, grid);
                }
            }
        }
        return ans;
    }
private: 
    void dfs(int x, int y, vector<vector<char>>& grid ) {
        int rows = (int)grid.size(), cols = (int)grid[0].size();
        grid[x][y] = '0';
        int dx[4] = {-1, 1, 0, 0};
        int dy[4] = {0, 0, -1, 1};
        for (int i = 0; i < 4; ++i) {
            int new_x = x + dx[i], new_y = y + dy[i];
            if (new_x >= 0 && new_x < rows && new_y >= 0 && new_y <cols && grid[new_x][new_y] == '1') {
            dfs(x + dx[i], y + dy[i], grid);
            }
        }
    }
};

class Solution {
public:
    int numIslands(vector<vector<char>>& g) {
        rows = g.size();
        if (!rows) return 0;
        cols = g[0].size();
        grid = &g;            // 记录指针避免频繁拷贝
        int ans = 0;

        for (int x = 0; x < rows; ++x)
            for (int y = 0; y < cols; ++y)
                if ((*grid)[x][y] == '1') {
                    ++ans;
                    dfs(x, y);                // 将整座岛全部改成 '0'
                }
        return ans;
    }
private:
    int rows{}, cols{};
    vector<vector<char>>* grid;               // 指向原网格
    static constexpr int dx[4] = {-1, 1, 0, 0};
    static constexpr int dy[4] = {0, 0, -1, 1};

    void dfs(int x, int y) {
        if (x < 0 || x >= rows || y < 0 || y >= cols ||
            (*grid)[x][y] != '1') return;
        (*grid)[x][y] = '0';                  // 访过即“沉岛”
        for (int k = 0; k < 4; ++k)
            dfs(x + dx[k], y + dy[k]);
    }
};
