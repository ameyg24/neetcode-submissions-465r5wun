class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        stack = []
        curr = []
# 1,2,2,4,5,6,9
        def dfs(i, currsum):
            if currsum >= target or i == len(candidates):
                if currsum == target:
                    stack.append(curr.copy())
                return
            curr.append(candidates[i])
            dfs(i+1, currsum + candidates[i])
            while i+1 in range(len(candidates)) and candidates[i] == candidates[i+1]:
                i+=1
            curr.pop()
            dfs(i+1, currsum)
        dfs(0,0)
        return stack
