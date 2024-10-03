class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)): 
            while stack and temperatures[i] > temperatures[stack[-1]]:
                tmp = stack.pop()
                res[tmp] = i-tmp
            stack.append(i)
        return res