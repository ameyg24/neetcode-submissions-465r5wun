class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n)
        # [0,0,0]
        if n <= 2:
            return n
        first, second = 1,2
        while n != 2:
            curr = first + second
            first = second
            second = curr
            n -= 1
        return second