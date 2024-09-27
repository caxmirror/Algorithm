class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [[-v, k] for k, v in count.items()]
        heapq.heapify(maxheap)
        prev = None # avoid being same
        res = ""

        while maxheap or prev:
            if not maxheap and prev:
                return ""
            v, k = heapq.heappop(maxheap)
            res += k
            if prev != None:
                heapq.heappush(maxheap, prev)

            if v < -1:
                prev = [v+1,k]
            else: 
                prev = None
        return res
    
    def reorganizeString2(self, s: str) -> str:
        count = Counter(s)
        count_sort = sorted(count.items(), key = lambda x:x[1], reverse = True)
        slist = [""]*len(s)

        i = 0
        for k, v in count_sort:
            if i == 0 and v > (len(s)+1) // 2:
                return ""
            while v > 0: 
                if i >= len(s):
                    i = 1
                slist[i] = k
                v -= 1
                i += 2
                
        return "".join(slist)