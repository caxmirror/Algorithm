# time: n
# space: n
class Solution_best:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i - k + 1 >= 0:
                res.append(nums[dq[0]])
        return res


# time: nlog2k
# space: 2k + n
class Solution_me:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window + max

        # 1.heap - dynamically maintain max heap?
        # 2.maxheap
        # 3.if I do not remove elements? 
        # 4.while loop check the top elements, if not meet condition, remove

        # 1.dic (sorted?)

        # [1,3,-1,-3,5,3,6,7], k = 3
        # 3,1,-1
        # (3,2),1,-1,-3
        # i = 3, k = 3
        maxheap = []
        res = []
        for i,num in enumerate(nums):
            heapq.heappush(maxheap,(-num,i))
            if len(maxheap) >= k:
                while maxheap[0][1] <= i - k:
                    heapq.heappop(maxheap)
                res.append(-maxheap[0][0])
        return res

