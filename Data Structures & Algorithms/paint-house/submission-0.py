class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0,0,0] for _ in range(n)]
        print(dp)
        dp[0] = costs[0]
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1] + costs[i][0], dp[i-1][2] + costs[i][0])
            dp[i][1] = min(dp[i-1][0] + costs[i][1], dp[i-1][2] + costs[i][1])
            dp[i][2] = min(dp[i-1][1] + costs[i][2], dp[i-1][0] + costs[i][2])
        print(dp)
        return min(dp[-1])