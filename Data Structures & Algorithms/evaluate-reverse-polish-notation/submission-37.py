class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {"+", "-", "/", "*"}
        for el in tokens:
            if el not in symbols:
                stack.append(el)
            else:
                symbol = el
                first = int(stack.pop())
                second = int(stack.pop())
                if symbol == "+":
                    res = first + second
                elif symbol == "-":
                    res = second - first
                elif symbol == "*":
                    res = first * second
                else:
                    res = second/first
                stack.append(res)
        print(stack)
        return int(stack[0])