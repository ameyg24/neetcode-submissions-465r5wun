class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        if n == 1:
            return 1 if int(s[0]) != 0 else 0
        if s[0] != "0":
            dp[0] = 1
        if s[1] != "0":
            dp[1] = dp[0]
        if s[0] == "1" or (s[0] == "2" and int(s[1]) < 7):
            dp[1] += 1
        print(dp)

        for i in range(2, n):
            if int(s[i]) != 0:
                dp[i] = dp[i-1]
            if int(s[i-1]) == 1 or (int(s[i-1]) == 2 and int(s[i]) < 7):
                dp[i] += dp[i-2]
        return dp[-1]


# 1 1 2 3
#  11 2 3
# 1 12 3
# 11 23
# 1 1 23