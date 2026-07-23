class Solution:
    def myPow(self, x: float, n: int) -> float:
        tmp = 1
        if n > 0:
            for _ in range(n):
                tmp = tmp * x
            return tmp
        else:
            for _ in range(-n):
                tmp = tmp * x
            return 1/tmp