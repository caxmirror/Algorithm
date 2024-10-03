class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        l = r = 0
        res = 0
        for i in range(1,len(s)):
            if ord(s[i]) == ord(s[i-1])+1:
                r+=1
            else:
                res = max(res,r-l+1)
                l = r = i
        return max(res,r-l+1)
        