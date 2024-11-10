# time: M
# space: M
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur_str, left_count, right_count):
            if len(cur_str) == n * 2:
                res.append(cur_str)
            else: 
                if left_count < n:
                    dfs(cur_str + "(", left_count+1,right_count)
                if right_count < left_count:
                    dfs(cur_str + ")", left_count,right_count+1)
        dfs("",0,0)
        return res

        