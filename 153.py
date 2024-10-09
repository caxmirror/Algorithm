class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        res=nums[0]

        while l <= r: 
            if nums[l] < nums[r]: 
                res = min(res,nums[l]) # trick here, need to use res to store the minimum 
                break 

            m = (l+r)//2
            res = min(res,nums[m]) 
            if nums[m] >= nums[l]: 
                l = m + 1
            else: 
                r = m - 1 
        return res

