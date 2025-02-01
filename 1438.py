# time: 2n
# space: 2n
class Solution_best_me:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxdq = deque()
        mindq = deque()
        left = 0
        res = 0
        for i in range(len(nums)):
            while (maxdq and abs(nums[maxdq[0]] - nums[i]) > limit) or (mindq and abs(nums[mindq[0]] - nums[i]) > limit):
                left += 1
                while maxdq and maxdq[0] < left:
                    maxdq.popleft()
                while mindq and mindq[0] < left:
                    mindq.popleft()
            while maxdq and nums[maxdq[-1]] < nums[i]:
                maxdq.pop()
            while mindq and nums[mindq[-1]] > nums[i]:
                mindq.pop()
            mindq.append(i)
            maxdq.append(i)
            res = max(res, i - left + 1)
        return res
        