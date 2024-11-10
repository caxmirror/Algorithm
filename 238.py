# time: n
# space: n

from typing import List

class Solution_chat:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 初始化结果数组
        res = [1] * len(nums)
        
        # Step 1: 计算每个元素的前缀乘积
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # Step 2: 计算每个元素的后缀乘积并与前缀乘积相乘
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res

# time: n
# space: n
class Solution_me:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use to list to store info
        prefix = [nums[0]] * len(nums)
        suffix = [nums[len(nums)-1]] * len(nums)
        res = [0] * len(nums)
        for i in range(1,len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
            suffix[len(nums) - i - 1] = nums[len(nums) - i - 1] * suffix[len(nums) - i]
        res[0] = suffix[1]
        res[len(nums)-1] = prefix[len(nums)-2]

        for i in range(1,len(nums)-1):
            res[i] = prefix[i-1] * suffix[i+1]
        return res
