class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Stack to store the indices
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push the index of '('
            else:
                stack.pop()  # Try to match the current ')' with the last unmatched '('
                if not stack:
                    stack.append(i)  # No matching '(', so push the index of ')'
                else:
                    max_length = max(max_length, i - stack[-1])  # Update max length of valid parentheses
        
        return max_length
