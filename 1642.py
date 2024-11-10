# time: n log k
# space: k
import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # approach1: dfs
        # approach2: heap better
        ladder_usage = [] # minHeap size of heap is important
        
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            
            if diff > 0:
                heapq.heappush(ladder_usage, diff)
                if len(ladder_usage) > ladders:
                    bricks -= heapq.heappop(ladder_usage)

            if bricks < 0:
                return i
            
        return len(heights) - 1

