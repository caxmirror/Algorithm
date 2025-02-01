# time: n
# space: 1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 
        # make sure each journey is ok
        # we have to calculate a lot of sum
        # prefix sum? with loop
        # 1,2,3,4,5
        # 1,3,6,10,15

        # 3,4,5,1,2
        # 3,7,12,13,15
        
        # diff
        # -2, -2, -2, 3, 3
        # find starting point: i_min_sum + 1
        # 
        n = len(gas)
        min_sum = float("inf")
        min_sum_index = 0
        cur_sum = 0
        for i in range(n):
            cur_sum += gas[i] - cost[i]
            if cur_sum < min_sum:
                min_sum = cur_sum
                min_sum_index = (i + 1) % n
        if cur_sum < 0:
            return -1
        return min_sum_index