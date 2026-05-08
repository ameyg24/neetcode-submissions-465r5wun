class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target/2
        sums = set()
        sums.add(0)
        for num in nums:
            nextdp = set()
            for el in sums:
                t = el + num
                if t == target:
                    return True
                nextdp.add(t)
                nextdp.add(el)
            sums = nextdp

        return False