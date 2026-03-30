class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            x = stones.pop()
            y = stones.pop()
            stones.append(max(x-y, y-x))
        if stones:
            return stones[0]
        return 0