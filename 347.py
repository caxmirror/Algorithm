class Solution:
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

