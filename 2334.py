# time: n
# space: n

# approach: 考的比较细，题目想找的是连续的比某个值大的subarray，所以要去找每个点的左右两侧>=它的边界，确定好边界后再检查是否满足要求即可，有点像灌水问题，注意是找>=的边界，跟sum完全没有任何关系，不要搞错方向了。找边界的话使用单调栈是不二之选

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        # monotonic stack
        # return nearest value smaller than current value
        n = len(nums)
        left_bound = [-1] * n
        right_bound = [n] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right_bound[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            if nums[i] > threshold / (right_bound[i] - left_bound[i] - 1):
                return right_bound[i] - left_bound[i] - 1
        
        return -1