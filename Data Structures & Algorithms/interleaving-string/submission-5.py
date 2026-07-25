class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[n][m] = True
        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                if i == n and j == m:
                    continue
                if i == n:
                    if s2[j] == s3[i + j]:
                        dp[i][j] = dp[i][j + 1]
                elif j == m:
                    if s1[i] == s3[i + j]:
                        dp[i][j] = dp[i+1][j]
                else:
                    if s1[i] == s3[i + j]:
                        dp[i][j] = dp[i+1][j]
                    if s2[j] == s3[i + j]:
                        dp[i][j] = dp[i][j+1]
        print(dp)
        return dp[0][0]

# [[0,0,0],
# [0,0,0]
# [0,0,0],
# [0,0,0]]
        
