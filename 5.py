class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = 1
        res = s[0]
        for i in range(len(s)):
            l=r=i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r-l+1
                if length > max:
                    max = length
                    res = s[l:r+1]
                l -= 1; r += 1
        for i in range(len(s)):
            l=i; r=i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r-l+1
                if length > max:
                    max = length
                    res = s[l:r+1]
                l -= 1; r += 1

        return res

