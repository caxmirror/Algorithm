class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens)-1
        res = 0
        result = 0
        while l <= r:
            if power - tokens[l] >= 0:
                power -= tokens[l]
                l += 1
                res += 1
                result = max(res,result)
            else: 
                if res == 0:
                    return 0
                power += tokens[r]
                r -= 1 
                res -= 1 
        return result
        