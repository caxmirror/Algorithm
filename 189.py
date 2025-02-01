# time: n
# space: 1
class Solution_best_me:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotate

        # 1,2,3,4 ,5,6,7
        # i = 4(6), k = 3 
        def rotate(a, b):
            for i in range(a, (b - a + 1) // 2 + a): # number of elem = b - a + 1; diff = b - a
                tmp = nums[i]
                nums[i] = nums[b + a - i] 
                nums[b + a - i] = tmp
        
        n = len(nums)-1
        if k != 0:
            k = k % (n + 1)
        k = n - k
        rotate(0,k)
        rotate(k+1,n)
        rotate(0,n)
        return nums