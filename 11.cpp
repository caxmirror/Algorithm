// time: n
// space: 1
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = (int)height.size() - 1; 
        int area = 0;
        while (l < r) {
            area = max(area, (r - l) * min(height[r], height[l]));
            if (height[l] > height[r]) {
                r -= 1;
            } else {
                l += 1;
            }
        }
        return area;
    }
};