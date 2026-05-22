class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        res = 0
        while r < n-1:
            far = 0
            for i in range(l, r + 1):
                far = max(far, i + nums[i])
            res += 1
            l, r = r+1, far
        return res