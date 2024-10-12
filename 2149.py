class Solution: 
    def rearrangeArray(self, nums: List[int]) -> List[int]: 
        dequepos = collections.deque()
        dequeneg = collections.deque()
        for i in range(len(nums)):
            if nums[i] > 0:
                dequepos.append(nums[i])
            else:
                dequeneg.append(nums[i])
        res = []
        for i in range(len(nums)//2):
            res.append(dequepos.popleft())
            res.append(dequeneg.popleft())
        return res
