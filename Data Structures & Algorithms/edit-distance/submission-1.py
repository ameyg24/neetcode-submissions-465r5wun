class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            dp[i][-1] = n-i
        for j in range(m-1,-1,-1):
            dp[-1][j] = m-j
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(1 + dp[i+1][j+1], 1 + dp[i+1][j], 1 + dp[i][j+1])
        return dp[0][0]
#    m o n e y
# m[[0,0,0,0,0,7]
# o[0,0,0,0,0,6]
# n[0,0,0,0,0,5]
# k[0,0,0,0,0,4]
# e[0,0,0,1,2,3]
# y[5,4,3,2,1,2]
# s[5,4,3,2,1,1]
#  [5,4,3,2,1,0]]