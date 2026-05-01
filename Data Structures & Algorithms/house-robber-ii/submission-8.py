class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        if n == 3:
            return max(nums[0],nums[1], nums[2])
        tmp = nums.copy()
        tmp = tmp[:n-1]
        tmp[2] = max(tmp[1], tmp[0] + tmp[2])
        for i in range(3, n-1):
            tmp[i] += max(tmp[i-2], tmp[i-3])
        nums = nums[1:]
        nums[2] = max(nums[1], nums[0] + nums[2])
        for i in range(3, n-1):
            nums[i] += max(nums[i-2], nums[i-3])
        print(tmp, nums)
        return max(nums[-1],nums[-2],tmp[-1],tmp[-2])
        