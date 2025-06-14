class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # just try to find all valid combinations, backtracking seems to be a good point to code
        # 这里面能优化的东西, 首先是剪枝把超范围的剪掉, 然后是传参的话, 尽量保持一个path避免多次复制
        res = []
        def backtrack(level, cur):
            if level == k and sum(cur)==n:
                res.append(cur)
                return
            if cur == []:
                for i in range(1, 10):
                    backtrack(1, [i])
            else:
                tmp = cur[-1]
                for i in range(tmp + 1, 10):
                    backtrack(level + 1, cur + [i])
        backtrack(0, [])
        return res