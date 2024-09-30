class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [] 
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                val = 0
                while stack and stack[-1] != 0:
                    val += stack.pop()
                stack.pop()
                stack.append(max(val*2,1))
        return sum(stack)