class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            diff = stones.pop()-stones.pop()
            if diff:
                stones.append(diff)
        if stones:
            return stones[0]
        return 0