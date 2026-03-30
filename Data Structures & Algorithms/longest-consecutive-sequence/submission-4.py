class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        maxcount = 0
        for el in nums:
            if el + 1 in sets:
                continue
            else:
                curr = 0
                while el in sets:
                    curr +=1
                    el = el - 1
                maxcount = max(maxcount, curr)
        return maxcount
