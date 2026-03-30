class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rdiag = set()
        ldiag = set()
        visited = set()
        def stringmaker(idx):
            tmp = ""
            for i in range(n):
                if i == idx:
                    tmp += "Q"
                else:
                    tmp += "."
            return tmp
        res = []
        curr = []
        def backtrack(r):
            if r == n:
                res.append(curr.copy())
                return
            for idx in range(n):
                if idx not in visited and (r+idx) not in rdiag and (r-idx) not in ldiag:
                    visited.add(idx)
                    rdiag.add(r+idx)
                    ldiag.add(r-idx)
                    curr.append(stringmaker(idx))
                    backtrack(r+1)
                    visited.remove(idx)
                    rdiag.remove(r+idx)
                    ldiag.remove(r-idx)     
                    curr.pop()    
        backtrack(0)
        return res        