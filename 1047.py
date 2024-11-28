# time: n
# space: n
class Solution_best_me:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack != [] and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)