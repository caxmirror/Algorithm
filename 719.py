# time: nlogn
# space: 1
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count_helper(distance):
            left = 0
            count = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > distance:
                    left += 1
                count += right - left
            return count
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (right + left) // 2
            if count_helper(mid) >= k:
                right = mid
            else: 
                left = mid + 1
        return left
