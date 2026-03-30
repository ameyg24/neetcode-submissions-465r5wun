class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2 :
            return max(nums)
        one, two = nums[-2],nums[-1]
        nums[-3] += nums[-1]
        for i in range(n-4,-1,-1):
            nums[i] += max(nums[i+2],nums[i+3])
            # print("x")
        return max(nums)
        