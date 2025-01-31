# time: n
# space: u
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for i in range(len(nums)-1, -1, -1):
            new_total = total - nums[i]
            if new_total % 2 == 0:
                target = new_total // 2
                if target in count:
                    if target != nums[i]:
                        return nums[i]
                    else: 
                        if count[target] >= 2:
                            return nums[i]