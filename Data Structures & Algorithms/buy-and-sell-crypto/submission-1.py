class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        L = 0
        R = 1
        diff = 0
        while (R != n):
            if prices[L] > prices[R] :
                L = R
                R+=1
            else:
                if prices[R] - prices[L] > diff:
                    diff = prices[R] - prices[L]
                R+= 1
        return diff