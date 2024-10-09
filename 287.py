class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0, 0
        while slow!=fast or slow ==0:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
