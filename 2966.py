class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)//3):
            if nums[i*3 + 2] - nums[i*3] > k:
                return []
            else:
                res.append([nums[i*3],nums[i*3+1],nums[i*3+2]])
        return res