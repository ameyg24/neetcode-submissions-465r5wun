class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        values = set(range(1,len(nums)))
        for el in nums:
            if el in values:
                values.remove(el)
            else:
                return el
        