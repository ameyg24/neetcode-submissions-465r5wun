class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def gp(op, cl, curr):
            if op == n and cl == n:
                tmp = curr.copy()
                string = "".join(tmp)
                res.append(string)
                return
            if op < n:
                curr.append("(")
                gp(op + 1, cl, curr)
                curr.pop()
            if op > cl and cl < n:
                curr.append(")")
                gp(op, cl + 1, curr)
                curr.pop()
        gp(0,0, [])
        return res
        