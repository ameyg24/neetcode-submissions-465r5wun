class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = ""
        res = []
        def dfs(left, right, curr):
            if left == right == n:
                res.append(curr)
                return
            if left > right and left <= n:
                curr += ")"
                dfs(left, right + 1, curr)
                curr = curr[:-1]
            if left < n:
                curr += "("
                dfs(left + 1, right, curr)
        dfs(0,0, "")
        return res
