class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxdp = mindp = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                tmp = maxdp
                maxdp = max(nums[i], nums[i]*mindp)
                mindp = min(nums[i], nums[i] * tmp)
            else:
                
                maxdp = max(nums[i], nums[i]*maxdp)
                mindp = min(nums[i], nums[i] * mindp)
            print(maxdp, mindp)
            res = max(res, maxdp)
        return res