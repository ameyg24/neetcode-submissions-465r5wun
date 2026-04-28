class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0],cost[1])     
        n = len(cost)
        first, second = cost[0], cost[1]
        count = 2
        while count < n:
            cost[count] = min(cost[count]+cost[count-2], cost[count] + cost[count-1])
            count +=1
        print(cost)
        return min(cost[-1],cost[-2])
