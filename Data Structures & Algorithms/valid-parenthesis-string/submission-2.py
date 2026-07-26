class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        cache = {}
        def dfs(idx, leftopen):
            if idx == n:
                return leftopen == 0
            if leftopen < 0:
                return False
            if (idx, leftopen) in cache:
                return cache[(idx, leftopen)]
            if s[idx] == "(":
                cache[(idx, leftopen)] = dfs(idx+1, leftopen + 1)
                return cache[(idx, leftopen)]
            elif s[idx] == ")":
                cache[(idx, leftopen)] = dfs(idx + 1, leftopen - 1)
                return cache[(idx, leftopen)]
            else:
                cache[(idx, leftopen)] = dfs(idx + 1, leftopen) or dfs(idx + 1, leftopen + 1) or dfs(idx + 1, leftopen - 1)
                return cache[(idx, leftopen)]
        return dfs(0, 0)


        