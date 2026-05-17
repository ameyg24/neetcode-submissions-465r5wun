class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for el in nums:
            res = res ^ el
        return res