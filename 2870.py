class Solution:
    def minOperations(self, nums: List[int]) -> int:
        maximum = 1
        mymap = {}
        for num in nums:
            if num not in mymap:
                mymap[num] = 1
            else:
                mymap[num] += 1
                maximum = max(maximum, mymap[num])
        
        cache = [0] * (maximum+1)
        cache[1] = float("inf")
        if len(cache) > 2: cache[2] = 1
        
        i = 3 
        while i < len(cache): 
            cache[i] = min(cache[i-2]+1, cache[i-3]+1) 
            i += 1 

        res = 0 
        for k, v in mymap.items(): 
            res += cache[v] 
        if res == float("inf"): 
            return -1 
        else: 
            return res 
            