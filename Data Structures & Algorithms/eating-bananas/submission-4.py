import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        higher = max(piles)
        while lower <= higher:
            middle = (lower + higher)//2
            count = 0
            for element in piles:
                count += math.ceil(float(element) / middle)
            if count <= h:
                higher = middle - 1
            else:
                lower = middle + 1
        return max(lower, higher)