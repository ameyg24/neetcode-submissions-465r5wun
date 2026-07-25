class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[n][m] = True

        for j in range(m-1):
            if p[j+1] == "*":
                dp[n][j] = dp[n][j+2]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if p[j] == "*":
                    continue
                elif j+1 < m and p[j+1] == "*":
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i+1][j+2] or dp[i+1][j] or dp[i][j+2]
                    else:
                        dp[i][j] = dp[i][j+2]
                else: 
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i+1][j+1]
                # elif p[j] == "*":
                #     if s[i] == 
                #     continue
                #     if s[i] == p[j-1] or p[j-1] == ".":
                #         dp[i][j] = dp[i+1][j+1] or dp[i+1][j]
                #     else:
                #         dp[i][j] = dp[i][j+1]

        print(dp)
        return dp[0][0]
#    n *
# n[[0,0,F]
# n[T,F,F]
# n[T,T,F]
#  [F,T,T]]
#   n      *
# n[False, False, False], 
# n[True, False, False], 
# n[True, True, False],
#  [False, True, True]]

#    .      *      z
# x [False, False, False, False], 
# y [False, False, False, False], 
# z [True, False, True, False], 
# [False, True, False, True]]

#    c      *     a     *     b
# a[[False, True, True, False, False, False], 
# a[True, False, True, False, False, False], 
# b[True, False, True, False, True, False],
# [False, False, False, False, False, True]]
# 
#   a       b      *
# a[[False, False, False, False], 
# [False, True, False, True]]

#   .      *      c
# a[[True, False, False, False], 
# b[True, False, False, False], 
# [True, False, False, True]]

#   .      *      a      *      a
# b[False, False, False, False, False, False], 
# b[False, False, False, False, False, False], 
# b[False, False, False, False, False, False], 
# b[False, False, False, False, False, False], 
# b[False, False, False, False, False, False], 
# a[False, False, False, False, True, False], 
# [False, False, False, False, False, True]]





        