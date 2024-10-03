class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                tmp = []
                multi = 0
                count = 1
                while stack[-1] != "[":
                    tmp.append(stack.pop())
                stack.pop()
                while stack and stack[-1] >= "0" and stack[-1] <= "9":
                    multi = int(stack.pop())*count + multi
                    count *= 10
                if count != 1:
                    tmp = tmp * multi
                while tmp:
                    stack.append(tmp.pop())
            else:
                stack.append(char)
        return "".join(stack)