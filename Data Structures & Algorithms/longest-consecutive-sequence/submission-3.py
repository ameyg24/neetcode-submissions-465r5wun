class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        maxval = 0
        for el in nums:
            if el+1 in visited:
                continue
            count = 1
            while el-1 in visited:
                count += 1
                el -= 1
            maxval = max(maxval, count)
        return maxval

                
