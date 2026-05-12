class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        sums = set()
        sums.add(0)
        for el in nums:
            tmp = sums.copy()
            for s in sums:
                tmp.add(s)
                tmp.add(s + el)
            sums = tmp
        return target in sums