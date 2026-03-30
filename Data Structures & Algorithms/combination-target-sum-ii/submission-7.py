class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        candidates.sort()
        def dfs(i, total):
            if total == target:
                if subset not in ans:
                    ans.append(subset.copy())
                return
            if total > target or i >= len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])
            subset.pop()
            while (i + 1 < len(candidates) and candidates[i] == candidates[i+1]) :
                i += 1
            dfs(i+1, total)
        dfs(0,0)
        return ans
        