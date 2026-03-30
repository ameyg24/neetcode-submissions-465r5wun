class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        higher = max(piles)
        ans = higher
        while lower <= higher:
            middle = (lower + higher)//2
            count = 0
            for element in piles:
                count += (element + middle - 1)//middle
            if count <= h:
                answer = middle
                higher = middle - 1
            else:
                lower = middle + 1
        return answer