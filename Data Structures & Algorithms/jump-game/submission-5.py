class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currpos = 0
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n-2,-1,-1):

            for j in range(1, nums[i] + 1):
                if not dp[i] and i + j < n:
                    dp[i] = dp[i + j]

        return dp[0]