import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        # def sign(one, two, string):
        #     if string == "+":
        #         return one + two
        #     elif string == "-":
        #         return one - two
        #     elif string == "*":
        #         return one*two
        #     elif string == "/":
        #         return one/two
        signs = {"+","-","*","/"}
        stack = []
        tmp = 0
        for i in range(n):
            # if i == n-1 and tokens[i] in signs:
            #     one = int(stack.pop())
            #     two = int(stack.pop())
            #     if tokens[i] == "+":
            #         res=one+two
            #         stack.append(res)
            #     elif tokens[i] == "-":
            #         res = two - one
            #         stack.append(res)
            #     elif tokens[i] == "*":
            #         res = one*two
            #         stack.append(res)
            #     elif tokens[i] == "/":
            #         res = one//two if two != 0 else 0
            #         stack.append(res)
            #     continue
            if tokens[i] not in signs:
                stack.append(int(tokens[i]))
            else:
                one = stack.pop()
                two = stack.pop()
                if tokens[i] == "+":
                    res=one+two
                    stack.append(res)
                elif tokens[i] == "-":
                    res = two-one
                    stack.append(res)
                elif tokens[i] == "*":
                    res = one*two
                    stack.append(res)
                elif tokens[i] == "/":
                    res = two/one if one != 0 else 0
                    stack.append(int(res))
            print(stack)
        return stack[-1]