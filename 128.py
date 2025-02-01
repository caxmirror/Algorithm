# 比较细致的hashset操作
# time: n
# space: n
class Solution_best:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set
        # loop through each num, if num - 1 exist, dont do any thing, if num + 1 exist, continue to loop. total: O (n)
        # 
        hashset = set(nums)
        res = 0
        for num in hashset:
            if num - 1 not in hashset:
                cur_num = num
                cur_res = 1
                while cur_num + 1 in hashset:
                    cur_num += 1
                    cur_res += 1
                res = max(res, cur_res)
        return res