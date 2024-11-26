# time: n
# space: 1
# approach: 之所以不需要找到i左右最大，如从左向右遍历时，找到当前点的左边最大值，并且右边大于左边即可，不需要找到右边最大值，这就是能优化的空间，因此不需要存下左右boundary，而是用two pointer即可做。
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        left_max = height[left]
        right_max = height[right]
        res = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += max(0, min(right_max, left_max) - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += max(0, min(right_max, left_max) - height[right])

        return res

# time: n
# space: n
class Solution_me_good:
    def trap(self, height: List[int]) -> int:
        # a: monotonic stack, find nearest smaller one
        # seems like not that complext to use monotonic stack
        # a: use max param to store highest

        n = len(height)
        left_bound = [0] * n
        right_bound = [0] * n
        res = [0] * n
        highest = 0

        for i in range(n): 
            if height[i] > highest:
                highest = height[i]
            left_bound[i] = highest

        highest = 0
        for i in range(n-1,-1,-1): 
            if height[i] > highest:
                highest = height[i]
            right_bound[i] = highest
            
        for i in range(n):
            a = min(left_bound[i], right_bound[i])
            res[i] = a - height[i]
        
        return sum(res)
            



