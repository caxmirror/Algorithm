class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tmp = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == tmp:
                count += 1
            else:
                count -= 1
                if count < 0:
                    tmp = nums[i]
                    count = 0
        return tmp