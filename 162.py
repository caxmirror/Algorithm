# time: nlogn
# space: 1
from typing import List

class Solution_best:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:  # Edge case: only one element
            return 0
        
        left, right = 0, n - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare mid with its next element
            if nums[mid] > nums[mid + 1]:
                # Mid is greater than the next element; move left
                right = mid
            else:
                # Mid is less than the next element; move right
                left = mid + 1
        
        # At the end of the loop, left == right, pointing to a peak
        return left


# time: nlogn
# space: 1
class Solution_best_me:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search + helper()
        n = len(nums) - 1
        if n == 0:
            return 0
        left, right = 0, n
        def condition(mid):
            if mid == 0:
                if nums[mid + 1] < nums[mid]:
                    return "m"
                else:
                    return "r"
            elif mid == n:
                if nums[mid - 1] < nums[mid]:
                    return "m"
                else:
                    return "l"
            else:
                if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                    return "m"
                elif nums[mid - 1] > nums[mid]:
                    return "l"
                else:
                    return "r"
        while left <= right:
            mid = (left + right) // 2
            if condition(mid) == "m":
                return mid
            elif condition(mid) == "l":
                right = mid - 1
            else:
                left = mid + 1
