class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return n
        count = [0] * n
        count[0] = 1
        count[1] = 2
        i = 2
        while i < n:
            count[i] = count[i-2] + count[i-1]
            i +=1
        return count[-1]

# [0,1,2,3]
# [0,1,2,3,5]