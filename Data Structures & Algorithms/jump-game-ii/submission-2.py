class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(False,float('inf'))] * (n)
        dp[-1] = (True,0)
        for i in range(n-2,-1,-1):
            for j in range(1,nums[i] + 1,1):
                if i + j <= n-1 and dp[i+j][0]:
                    dp[i] = (True, min(1 + dp[i+j][1], dp[i][1]))
        return dp[0][1]