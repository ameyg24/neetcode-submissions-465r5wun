class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)
        maxval = 0
        tmp = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                tmp += 1
            elif nums[i] - nums[i-1] == 0:
                continue
            else:
                if tmp > maxval : maxval = tmp
                tmp = 1
        if tmp > maxval : maxval = tmp
        return maxval