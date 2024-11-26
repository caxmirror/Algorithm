# time: n
# space: n
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # i j k
        # i < k < j
        # approach 1: j is nearest bigger num to k
        # i is the farest smaller value to k?? 

        # approach 2.从i的视角看，找最近的的j和较远的没那么大的(都应该在monotonic stack中) 

        # approach 3.trick: pop出去的value 用k记下来，因为是最远的，而且也是次大的

        n = len(nums)
        k_value = float('-inf')
        stack = []

        for i in range(n-1,-1,-1):
            if nums[i] < k_value: 
                return True
            while stack and stack[-1] < nums[i]: # 保证k是最远的，因此相等不换
                k_value = stack.pop()
            stack.append(nums[i])
        return False