# time: n
# space: n
class Solution_better_me:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: y-x,
            "*": lambda x,y: x*y,
            "/": lambda x,y: int(y/x)
        }

        stack = []
        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(op[token](num1,num2))
        return stack[-1]

# time: n
# space: n
class Solution_me:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ["+","-","*","/"] 
        def helper(op,num1,num2): 
            if op == "+": 
                return num1 + num2
            elif op == "-": 
                return num2 - num1
            elif op == "*": 
                return num1 * num2
            else: 
                return num2 // num1 + 1 if num2 / num1 < 0 and num2 % num1 != 0 else num2 // num1

        stack = []
        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(helper(token,num1,num2))
        return stack[-1]
        
