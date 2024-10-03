class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        # conversion: 
        # score: sum of conversion
        # return: score of prefix
        maxi = nums[0]
        for i in range(len(nums)):
            maxi = max(maxi,nums[i])
            nums[i] += maxi
            if i != 0:
                nums[i] += nums[i-1]
        return nums