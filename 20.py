class Solution:
    def isValid(self, s: str) -> bool:
        mymap = {")":"(","}":"{","]":"["}
        stack = []
        for char in s:
            if char in mymap:
                if stack and mymap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False