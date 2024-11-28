# time: n logk
# space: k
import heapq
class Solution_best:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        nitems = heapq.nlargest(k, count.items(), key = lambda x:x[1])

        return [key for key, value in nitems]

# time: n logn
# space: n
class Solution_me:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = dict(sorted(count.items(), key=lambda x:x[1], reverse = True))
        res = []
        for key, value in sorted_count.items():
            if(k>0):
                res.append(key)
                k -= 1
        return res

class Solution_me_worst:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        count_sorted = sorted(count.items(), key= lambda x:x[1], reverse=True)
        res = []
        for i,v in count_sorted:
            res.append(i)
        return res[0:k]

