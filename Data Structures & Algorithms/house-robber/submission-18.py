class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        nums[2] = max(nums[1], nums[0] + nums[2])
        for i in range(3, n):
            nums[i] += max(nums[i-3], nums[i-2])
        print(nums)
        return max(nums[-1], nums[-2])
