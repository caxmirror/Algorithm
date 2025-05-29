class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // set to store the char
        // because s consists of English letters, digits, symbols and spaces.
        // I can use Ascii code to directly access a vector, no need to use set.
        vector<int> pos(256, -1);
        int left = 0, ans = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            unsigned char c = s[i];
            if (pos[c] >= left) {
                left = pos[c] + 1;
            }
            pos[c] = i;
            ans = max(ans, i - left + 1);
        }
        return ans;
    }
};

// using map
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map;
        map.reserve(s.size()); //预分配减少reharsh
        int left = 0, ans = 0;
        for (int right = 0; right < (int)s.size(); ++right) {
            char c = s[right];
            if (map.count(c) && map[c] >= left) {
                left = map[c] + 1;
            }
            map[c] = right;
            ans = max(ans, right - left + 1);
        }
        return ans; 
    }
};

//use set erase and insert, a little bit slower than directly access the vector or use map
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // set to store the char
        // because s consists of English letters, digits, symbols and spaces.
        // I can use Ascii code to directly access a vector, no need to use set.
        unordered_set<char> set;
        int left = 0, ans = 0;
        for (int right = 0; right < (int)s.size(); right++) {
            while (set.count(s[right])) {
                set.erase(s[left++]);
            }
            set.insert(s[right]);
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};

