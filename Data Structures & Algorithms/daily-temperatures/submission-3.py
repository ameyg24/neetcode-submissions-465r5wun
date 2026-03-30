class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures: return []
        n= len(temperatures)
        res = [0]*n
        stack = []
        for i, temp in enumerate(temperatures):
            print(stack)
            while stack and temp > stack[-1][1]:
                days, t = stack.pop()
                res[days] = i-days
            stack.append((i,temp))
        return res
# 38,