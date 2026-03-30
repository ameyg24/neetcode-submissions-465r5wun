class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first, second = 0,0
        n = len(nums)
        tmp = nums.copy()
        for i in range(n-1):
            curr = max(tmp[i] + first, second)
            first = second
            second = curr
        t = second
        first, second = 0,0
        for i in range(1,n):
            curr = max(nums[i] + first, second)
            first = second
            second = curr
        return max(t, second)