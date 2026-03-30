class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l = 0
        # r = 1
        maxdiff = 0
        for r in range(1, len(prices)):
            maxdiff = max(maxdiff, prices[r]-prices[l])
            if prices[r] < prices[l]:
                l = r
        return maxdiff

        # while l <= r and r < len(prices) -1:
        #     maxdiff = max(maxdiff, prices[r]-prices[l])
        #     print(maxdiff , l, r)
        #     if prices[l] >= prices[l+1]:
        #         l+=1
        #     elif r+1 in range(len(prices)) and prices[r+1] >= prices[r]:
        #         r+=1
        # return maxdiff