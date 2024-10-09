class Solution:
    def __init__(self):
        self.res = 0
    def longestSubstring(self, s: str, k: int) -> int:
        mymap = {}
        reduceli = []
        for i,c in enumerate(s):
            if c not in mymap:
                mymap[c] = [i]
            else:
                mymap[c].append(i)
        for char, count in mymap.items():
            if len(count) < k:
                reduceli.extend(count)
        tmp = 0
        red = len(s)
        if not reduceli:
            return len(s)
        for red in reduceli: 
            self.res = max(self.res, self.longestSubstring(s[tmp:red], k)) 
            tmp = red+1
        self.res = max(self.res, self.longestSubstring(s[tmp:], k))
        return self.res