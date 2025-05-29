class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = (int)s1.size(), n2 = (int)s2.size();
        if (n1 > n2) {
            return false;
        }
        unordered_map<char, int> map1, map2;
        for (char c:s1) {
            map1[c] += 1;
        }
        int left = 0, right = left + n1;
        for (int i = left; i < right; ++i) {
            map2[s2[i]] += 1;
        }
        while (right < n2) {
            if (map2 == map1) { // can I do this? 
                return true;
            }
            map2[s2[left]] -= 1;
            if (map2[s2[left]] == 0) {
                map2.erase(s2[left]);
            }
            left++;
            map2[s2[right++]] += 1;
        }
        if (map2 == map1) { 
                return true;
            }
        return false;
    }
};