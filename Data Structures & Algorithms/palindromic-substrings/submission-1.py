class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    if i-j <= 2 or dp[i-1][j+1]:
                        dp[i][j] = True
                        res +=1
        return res