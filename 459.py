#time: n
#space: n
class Solution_best:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled = (s + s)[1:-1]
        return s in doubled

#time: n^2
#space: n
class Solution_me:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # find nums that can be divide by lens
        for i in range(1,len(s)):
            if len(s) % i == 0:
                if s == s[:i] * (len(s)//i):
                    return True
        return False
                