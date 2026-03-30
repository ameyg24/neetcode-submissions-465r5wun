class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n)
        # [0,0,0]
        if n <= 2:
            return n
        res[-1] = 1
        res[-2] = 2
        for i in range(n-3,-1,-1):
            res[i] = res[i+1] + res[i+2]
        return res[0]