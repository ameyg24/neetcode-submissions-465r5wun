class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = ""
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j] and (j-i+1) > len(res):
                    res = s[i:j+1]
        return res

