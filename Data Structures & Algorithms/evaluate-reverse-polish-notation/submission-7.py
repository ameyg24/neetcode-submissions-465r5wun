class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 2:
            for i in range(len(tokens)):
                operator = tokens[i]
                if operator in "+-*/":
                    first = float(tokens[i-2])
                    second = float(tokens[i-1])
                    if operator == "+":
                        tmp = int(first+second)
                    elif operator == "-":
                        tmp = int(first-second)
                    elif operator == "*":
                        tmp = int(first*second)
                    else:
                        tmp= int(first/second)
                    tokens = tokens[:i-2] + [str(tmp)] + tokens[i+1:]
                    break
                else:
                    continue
        return int(tokens[0])
            
        
