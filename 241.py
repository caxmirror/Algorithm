class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        op = { 
        "+": lambda x, y: x+y, 
        "-": lambda x, y: x-y, 
        "*": lambda x, y: x*y} 

        def backtracking(left, right): 
            res = []
            for i in range(left, right+1): 
                if expression[i] in op: 
                    nums1 = backtracking(left, i-1) 
                    nums2 = backtracking(i+1,right)

                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(op[expression[i]](n1,n2))
            if res == []:
                res.append(int(expression[left:right+1]))
            return res
        return backtracking(0,len(expression)-1)

