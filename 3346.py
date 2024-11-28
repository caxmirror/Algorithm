# 看sliding window



class Solution_FAILED: 
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int: 
        nums.sort() 
        left, right = 0, 0 
        res = 1 
        cur_same = 0 
        cur_2k = 0 

        while left < len(nums):
            # handle now 

            if right < len(nums) - 1:
                right += 1
            if nums[right] == nums[right - 1]:
                cur_same += 1
            print(left, right, abs(nums[right] - nums[right - 1]), (right - left - cur_same + cur_2k))
            if abs(nums[right] - nums[right - 1]) <= 2 * k: 
                if abs(nums[right] - nums[right - 1]) >= k: 
                    cur_2k += 1
                if abs(nums[right] - nums[left]) <= 2 * k:
                    print(left, right, abs(nums[right] - nums[right - 1]), (right - left - cur_same + cur_2k))
                    op_need = right - left - cur_same + cur_2k # cur_same
                    if numOperations >= op_need:
                        res = max(res, right - left + 1)
                else: 
                    print("+1")
                    left += 1
                    if nums[left] == nums[left - 1]:
                        cur_same -= 1
                    if k <= abs(nums[left] - nums[left - 1]) <= 2*k:
                        cur_2k -= 1   
            else: 
                print("jump")
                left = right
                cur_same = 0
        return res