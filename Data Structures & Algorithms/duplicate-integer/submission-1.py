class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = set(nums)
        return len(t) != len(nums)