# time: nlogk
# space: k
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k - most - heap
        # maxheap to store k min
        maxheap = []
        def distance(point):
            return point[0]**2 + point[1]**2

        for point in points:
            heapq.heappush(maxheap,[-distance(point), point])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        res = []
        while maxheap:
            res_distance, res_point = heapq.heappop(maxheap)
            res.append(res_point)
        return res