class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s)-1
        res = 0
        if s[l] != s[r]:
            return len(s)
        while l < r and s[l] == s[r]:
            while l < r-1 and s[l+1] == s[r]:
                l += 1
                res += 1
            while l < r-1 and s[r-1] == s[r]:
                r -= 1
                res += 1
            l += 1
            r -= 1
            res += 2
        return len(s) - res

            