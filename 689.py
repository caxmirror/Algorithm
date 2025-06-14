class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # start from the back cal sum of k in another array
        # make sure the 3 starting points are not overlapped and max sum
        # just sort, if collide, skip that. This could be the best solution
        tmp = []

        left = 0
        sum = 0 
        for right in range(len(nums)):
            while right - left >= k:
                sum -= nums[left]
                left += 1
            sum += nums[right]
            if right - left == k - 1:
                tmp.append(sum) # tmp should start from k

        left_best = []
        max_index = 0
        max_sum = 0
        for i in range(len(tmp)):
            if tmp[i] > max_sum:
                max_index = i
                max_sum = tmp[i]
            left_best.append(max_index)
        

        right_best = [0 for i in range(len(tmp))]
        max_index = 0
        max_sum = 0
        for i in range(len(tmp)-1,-1,-1):
            if tmp[i] >= max_sum:
                max_index = i
                max_sum = tmp[i]
            right_best[i] = max_index
        
        mid_best = []
        max_sum = 0
        res = []
        for i in range(k, len(tmp)-k):
            cur_sum = tmp[i] + tmp[left_best[i - k]] + tmp[right_best[i + k]]
            if max_sum < cur_sum:
                res = [left_best[i - k], i, right_best[i + k]]
                max_sum = cur_sum
        return res