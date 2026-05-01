class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        tmp = nums.copy()
        tmp = tmp[1:]
        nums = nums[:n-1]
        tmp[1] = max(tmp[0],tmp[1])
        for i in range(2, n-1):
            tmp[i] = max(tmp[i] + tmp[i-2], tmp[i-1])
        nums[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        return max(nums[-1], tmp[-1])