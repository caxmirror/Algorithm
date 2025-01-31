# time: n
# space: n

class Solution_best_me:
    def calculate(self, s: str) -> int:
        # interger divsion
        # stack to store nums and calculator
        # * / calculate immidiately
        # + - calculate in the end
        
        op_stack = deque()
        num_stack = deque()
        op = {"+": lambda a, b: a + b, 
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b, 
        "/": lambda a, b: int(a / b)}
        pointer = 0
        while pointer < len(s):
            ch = s[pointer]
            if ch.isdigit():
                left_pointer = pointer
                while pointer < len(s) and s[pointer].isdigit():
                    pointer += 1
                int_ch = int(s[left_pointer:pointer])
                num_stack.append(int_ch)
            elif ch == "*" or ch == "/":
                left_pointer = pointer
                pointer += 1
                if s[pointer] == " ":
                    pointer += 1
                left_pointer = pointer
                while pointer < len(s) and s[pointer].isdigit():
                    pointer += 1
                int_ch = int(s[left_pointer:pointer])
                num1 = num_stack.pop()
                num2 = int_ch
                result = op[ch](num1, num2)
                num_stack.append(result)
            elif ch == "+" or ch == "-":
                op_stack.append(ch)
                pointer += 1
            else:
                pointer += 1

        while op_stack:
            op_end = op_stack.popleft()
            num3 = num_stack.popleft()
            num4 = num_stack.popleft()
            num5 = op[op_end](num3, num4)
            num_stack.appendleft(num5)
        return num_stack[0]