class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        n = len(nums)
        def dfs(i):
            if i == n:
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            while i+1 in range(n) and nums[i]==nums[i+1]:
                i +=1
            dfs(i+1)

        dfs(0)
        return res