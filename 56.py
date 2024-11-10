# time: n logn
# space: n
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort with start
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        i = 0
        res = []
        while i < len(intervals):
            while i < len(intervals) - 1 and sorted_intervals[i][1] >= sorted_intervals[i+1][0]:
                sorted_intervals[i+1][0] = sorted_intervals[i][0]
                sorted_intervals[i+1][1] = max(sorted_intervals[i][1], sorted_intervals[i+1][1])
                i += 1
            res.append(sorted_intervals[i])
            i += 1
        return res
