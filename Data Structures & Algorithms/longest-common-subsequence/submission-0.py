class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [([0] * (n + 1)) for _ in range(m + 1)]
        # dp[2][4] = 1
        # print(dp)
        # return 0
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[j][i] = 1 + dp[j + 1][i + 1]
                else:
                    dp[j][i] = max(dp[j + 1][i], dp[j][i + 1])
        return dp[0][0]