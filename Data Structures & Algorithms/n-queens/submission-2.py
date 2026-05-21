class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        indices = set()
        rightdiag = set()
        leftdiag = set()
        curr = []
        res = []
        def maker(curr):
            res = []
            for i in range(n):
                tmp = ""
                for j in range(n):
                    if curr[i] == j:
                        tmp += "Q"
                    else:
                        tmp += "."
                res.append(tmp)
            return res
        def backtrack(i):
            if i == n:
                print(curr)
                t = maker(curr)
                res.append(t)
            for idx in range(n):
                if idx not in indices and (idx+i) not in rightdiag and (i - idx) not in leftdiag:
                    curr.append(idx)
                    rightdiag.add(idx+i)
                    leftdiag.add(i-idx)
                    indices.add(idx)
                    backtrack(i + 1)
                    curr.pop()
                    rightdiag.remove(idx+i)
                    leftdiag.remove(i-idx)
                    indices.remove(idx)
        backtrack(0)
        return res
            