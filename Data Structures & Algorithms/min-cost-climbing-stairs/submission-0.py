class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = cost[n-2], cost[n-1]
        t = 10**100
        for i in range(n-2):
            temp = one
            one = min(one + cost[n-3-i], two + cost[n-3-i])
            two = temp
        
        return min(one,two)
        