# t: 26 * n = n
# s: 26 * n = n
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mymap = {} # ,26 
        resset = set() # ,26 
        res = 0 

        for i in range(len(s)): # n, 26
            if s[i] not in mymap:
                mymap[s[i]] = [i,i]
            else:
                mymap[s[i]][1] = i
        
        for k,v in mymap.items(): # 26, 1
            l = v[0]
            r = v[1]
            for i in range(l+1,r): # n, 1
                tmp = k + s[i]+ k 
                if tmp not in resset:
                    resset.add(tmp) #, 26*n
                    res += 1
        return res