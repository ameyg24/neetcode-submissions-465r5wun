class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sums = sum(nums)
        print(sums)
        for i in range(len(nums) + 1):
            sums -= i
            print(i, sums)
        return -sums
        