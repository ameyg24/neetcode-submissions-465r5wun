class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        stack = []
        curr = []
        def dfs(i, currsum):
            if currsum >= target or i == len(nums):
                if currsum == target:
                    stack.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i, currsum + nums[i])
            curr.pop()
            dfs(i+1, currsum)
        dfs(0,0)
        return stack