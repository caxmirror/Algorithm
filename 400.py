class Solution:
    def findNthDigit(self, n: int) -> int:
        total = 9
        tmp = 9
        p = 1
        while True:
            
            if n <= total:
                
                remainder = (n - total + tmp - 1) % p
                quotient = (n - total + tmp - 1) // p
                
                base = quotient + pow(10,p-1)
                base = str(base)
                return int(base[remainder])
                
            tmp = 9 * pow(10,p) * (p+1)
            total += tmp
            p += 1
            

