#time: n
#space: n
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(","}":"{","]":"["}
        stack = []
        for ch in s:
            if ch not in dic:
                stack.append(ch)
            else:
                if stack == [] or dic[ch] != stack.pop():
                    return False
        if stack != []:
            return False
        return True
    
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