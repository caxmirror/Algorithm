// time: m * n * 3 ^ word.len() 三个方向
// space: L 递归深度

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        // 1. DFS or backtracking
        // 2.can not use it twice
        for (int x = 0; x < board.size(); x++) {
            for (int y = 0; y < board[0].size(); y++) {
                if (board[x][y] == word[0]) {
                    int index = 1;
                    if (dfs(board, index, word, x, y)) return true;
                }
            } 
        }
        return false;
    }

private: 
    bool dfs(vector<vector<char>>& board, int& index, const string& word, int x, int y) {
        if (index == word.size()) return true;
        int dx[4] = {0, 0, 1, -1}, dy[4] = {1, -1, 0, 0};
        bool res = false;
        for (int i = 0; i < 4; i++) {
            int new_x = x + dx[i]; 
            int new_y = y + dy[i]; 
            if (new_x >= 0 && new_x < board.size() && new_y >= 0 && new_y < board[0].size() && board[new_x][new_y] == word[index]) {
                char tmp = board[x][y];
                board[x][y] = '0';
                index++;
                if (dfs(board, index, word, new_x, new_y)) return true;
                index--;
                board[x][y] = tmp;
            }
        }
        return false;
    }
};