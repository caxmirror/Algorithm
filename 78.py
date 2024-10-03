class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i in range(0,len(nums)):
            lensubsets = len(subsets)
            for subseti in range(lensubsets):
                s = subsets[subseti].copy()
                s.append(nums[i])
                subsets.append(s)
        return subsets