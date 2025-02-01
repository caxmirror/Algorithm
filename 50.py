# time: logn
# space: logn
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # math
        # dp
        # hex
        # list 
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        res = 1

        dp = [x] 
        i = 0
        k = 1
        sum_k = 1
        res = 1
        while sum_k <= n:
            dp.append(dp[-1]**2)
            k *= 2
            sum_k += k
            i += 1
        while n != 0:
            if n >= k:
                n -= k
                res *= dp[i]
            i -= 1
            k /= 2
        return res