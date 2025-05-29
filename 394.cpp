//DFS 做法更简单 
class Solution {
public:
    string decodeString(string s) {
        int i = 0;
        return dfs(i, s);
    }
private: 
    string dfs(int & i, const string & s) {
        int k = 0;
        string curr = "";
        while (i < (int)s.size()) {
                if (isdigit(s[i])) {
                k = 10 * k + (s[i] - '0');
                i += 1;
            } else if (s[i] == '[') {
                i += 1;
                string tmp = dfs(i, s);
                while (k > 0) {
                    curr += tmp;
                    k--;
                }
            } else if (s[i] == ']') {
                i += 1;
                return curr;
            } else {
                curr += s[i];
                i += 1;
            }
        }
        return curr;
    }
};

class Solution {
public:
    string decodeString(string s) {
        stack<int> counts;
        stack<string> results;
        string curr;
        int k = 0;

        for (char c : s) {
            if (isdigit(c)) {
                k = 10 * k + c - '0';
            }
            else if (c == '[') {
                counts.push(k);
                results.push(curr);
                k = 0;
                curr.clear();
            }
            else if (c == ']') {
                int times = counts.top(); counts.pop();
                string prev = results.top(); results.pop();

                string tmp;
                tmp += prev;
                while(times-- > 0) {
                    tmp += curr;
                }
                curr = move(tmp);
            }
            else {
                curr += c;
            }

        }
        return curr;

    }
};