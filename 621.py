# time: nlogk
# space: k
# n - total task, k - unique task
class Solution_best:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for task in tasks:
            if task not in dic:
                dic[task] = 0
            dic[task] += 1
        
        max_heap = []
        for task, count in dic.items():
            max_heap.append(-count)
        heapq.heapify(max_heap) 

        cooldown = deque()
        time = 0
        while max_heap or cooldown:
            time += 1
            if max_heap:
                neg_count = heapq.heappop(max_heap) + 1 
                if neg_count != 0: 
                    cooldown.append([neg_count, time + n]) 
            if cooldown and cooldown[0][1] == time: 
                count_cooldown, _ = cooldown.popleft() 
                heapq.heappush(max_heap, count_cooldown) 
        return time 