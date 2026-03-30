import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # total = 0
        # if max(piles) > h:
        #     for p in piles:
        #         total += math.ceil(p/h)
        #     return total
        l, r = 1, max(piles)
        minimum = float("inf")
        while l <= r:
            mid = (l+r)//2
            total = 0
            for p in piles:
                total += math.ceil(p/mid)
            if total <= h:
                minimum = min(minimum, mid)
                r = mid - 1
            else:
                l = mid + 1
            
        return minimum