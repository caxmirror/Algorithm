class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        li = []
        for i in range(1,10): #0 - 9
            litmp = [i]
            for j in range(i+1,10): # i - 10
                litmp.append(litmp[-1]*10 + j)
            li.extend(litmp)
        li.sort()
        l, r = 0, len(li)-1
        while l <= len(li)-1 and li[l] < low:
            l += 1
        while li[r] > high:
            r -= 1
        return li[l:r+1]