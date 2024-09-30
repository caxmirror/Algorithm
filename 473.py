class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        sides = [0]*4
        target = total//4

        matchsticks.sort(reverse=True)
        def dfs(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return dfs(0)