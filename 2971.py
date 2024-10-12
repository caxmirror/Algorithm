class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        for i in range(len(nums)-1,-1,-1):
            total = total - nums[i]
            if nums[i] < total:
                return total + nums[i]
        return -1