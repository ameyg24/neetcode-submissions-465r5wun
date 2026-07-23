class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][-1] = 1
        for i in range(n-1,-1,-1):
            for j in range(amount-1,-1,-1):
                if j + coins[n - 1 - i] <= amount:
                    dp[i][j] = dp[i+1][j] + dp[i][j + coins[n - 1 - i]]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]
# [[4, 3, 2, 1, 1], 1
# [1, 1, 1, 0, 1], 2
# [0, 1, 0, 0, 1], 3
# [0, 0, 0, 0, 0]]
