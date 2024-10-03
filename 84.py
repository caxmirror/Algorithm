class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, (i - index)*height)
                start = index
            stack.append((start,h))
        for i, h in stack:
            res = max(res, (len(heights) - i)*h)
        return res