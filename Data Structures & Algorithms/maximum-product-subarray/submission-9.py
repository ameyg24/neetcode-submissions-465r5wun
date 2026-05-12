class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxval = minval = nums[0]
        res = nums[0]
        for i in range(1, n):
            tmp = maxval
            maxval = max(maxval * nums[i], minval * nums[i], nums[i])
            minval = min(tmp * nums[i], minval * nums[i], nums[i])
            res = max(res, maxval)
        return res