class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                res.append(s[i])
            elif s[i] == ")":
                if stack:
                    stack.pop()
                    res.append(s[i])
                else:
                    res.append("")
            else:
                res.append(s[i])
        for i in stack:
            res[i] = ""
        return "".join(res)
