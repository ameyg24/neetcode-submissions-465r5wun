class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        n = len(nums)
        def dfs(i, currsum):
            if i >= n or currsum >= target:
                if currsum == target:
                    res.append(curr.copy())
                    return
                else:
                    return
            curr.append(nums[i])
            dfs(i, currsum + nums[i])
            curr.pop()
            dfs(i + 1, currsum)

        dfs(0,0)
        return res

        