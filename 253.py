# time: n logn
# space: n
import heapq
class Solution_me:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        end_time = [sorted_intervals[0][1]]

        # use minheap to store the minmum
        for i in range(1, len(intervals)):
            
            if sorted_intervals[i][0] >= end_time[0]:
                heapq.heappop(end_time)
            
            heapq.heappush(end_time, sorted_intervals[i][1])
        return len(end_time)
