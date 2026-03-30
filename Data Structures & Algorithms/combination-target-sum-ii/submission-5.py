class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        def dfs(i, total):
            if total == target:
                tmp = subset.copy()
                tmp.sort()
                if tmp not in ans:
                    ans.append(tmp.copy())
                return
            if total > target or i >= len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])
            subset.pop()
            dfs(i+1, total)
        dfs(0,0)
        return ans
        