class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        nums[-3] += nums[-1]
        if n > 3:
            for i in range(n-4,-1,-1):
                nums[i] += max(nums[i+2],nums[i+3])
        
        return max(nums[0],nums[1])
