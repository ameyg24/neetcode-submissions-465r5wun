class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            operator = tokens[i]
            if operator in "+-*/":
                second = stack.pop()
                first = stack.pop()
                if operator == "+":
                    stack.append(int(first+second))
                elif operator == "-":
                    stack.append(int(first-second))
                elif operator == "*":
                    stack.append(int(first*second))
                else:
                    stack.append(int(float(first)/second))
            else:
                stack.append(int(tokens[i]))
        return int(stack[0])
            
        
