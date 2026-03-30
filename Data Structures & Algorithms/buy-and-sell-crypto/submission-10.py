class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maxprofit = 0
        n = len(prices)
        while i < n-1:
            if prices[i] > prices[i+1]:
                i+=1
            else:
                j = i+1
                while j in range(n-1) and prices[i] <= prices[j+1]:
                    maxprofit = max(maxprofit, prices[j]-prices[i])
                    j+=1
                maxprofit = max(maxprofit, prices[j]-prices[i])
                i = j
        return maxprofit