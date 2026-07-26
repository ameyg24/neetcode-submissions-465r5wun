class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        if sum(diff) < 0:
            return -1
        sums = 0
        last = -1
        print(diff)
        for i in range(len(diff)):
            sums += diff[i]
            if sums < 0:
                sums = 0
                last = i
        return last + 1
