class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr = []
        res = []
        n = len(candidates)
        def dfs(i, currsum):
            if i >= n or currsum >= target:
                if currsum == target:
                    res.append(curr.copy())
                    return
                else:
                    return
            curr.append(candidates[i])
            dfs(i+1, currsum + candidates[i])
            curr.pop()
            while i+1 in range(n) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i + 1, currsum)
        dfs(0,0)
        return res