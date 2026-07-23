class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        visit = set(nums)
        for i in range(len(nums) + 1):
            print(i, visit)
            if i not in visit:
                return i