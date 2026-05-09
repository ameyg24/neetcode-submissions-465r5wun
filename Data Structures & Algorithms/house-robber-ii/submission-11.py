class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0], nums[2], nums[1])
        tmp = nums[::]
        tmp.pop()
        tmp[2] = max(tmp[1], tmp[0] + tmp[2])
        for i in range(3, n-1):
            tmp[i] += max(tmp[i-2], tmp[i-3])
        nums[3] = max(nums[2], nums[3] + nums[1])
        for i in range(4, n):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2], tmp[-1], tmp[-2])