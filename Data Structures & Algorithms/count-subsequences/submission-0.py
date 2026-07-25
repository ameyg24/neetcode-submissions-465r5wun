class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # using s[i:] how many subsets can you make that are equal to t[j:]
        for i in range(n + 1):
            dp[i][-1] = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        print(dp)
        return dp[0][0]
#    c a t
# c[[3,3,1,1],
# a[0,3,1,1],
# a[0,2,1,1],
# a[0,1,1,1],
# t[0,0,1,1],
# [0,0,0,1]]

#    x y
# x[[5,2,1],
# x[3,2,1],
# y[1,2,1],
# x[1,1,1],
# y[0,1,1],
#  [0,0,1],]
