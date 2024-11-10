# time: n
# space: n
class Solution_best:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

# time: n
# space: n
class Solution_me:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = words[len(words)-1]
        for i in range(len(words)-2,-1,-1):
            res = res + " " + words[i]
        return res