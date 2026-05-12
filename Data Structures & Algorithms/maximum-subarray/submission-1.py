class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxval = nums[0]
        currsum = 0
        for n in nums:
            if currsum < 0:
                currsum = 0
            currsum += n
            maxval = max(maxval, currsum)
        return maxval