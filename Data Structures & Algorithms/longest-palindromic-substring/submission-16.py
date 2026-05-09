class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxidx = [0,0]
        for i in range(n):
            for j in range(i,-1, -1):
                if s[i] == s[j]:
                    if i-j <= 2 or dp[i-1][j+1]:
                        dp[i][j] = True
                        if (i - j+1) > (maxidx[1] - maxidx[0]):
                            maxidx[1], maxidx[0] = i, j
        return s[maxidx[0] : maxidx[1] + 1]


