class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        candidates.sort()
        def func(i, currsum):
            if currsum >= target or i >= len(candidates):
                if currsum == target:
                    res.append(arr.copy())
                    return
                else:
                    return
            arr.append(candidates[i])
            func(i+1, currsum + candidates[i])
            arr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            func(i+1, currsum)
        func(0,0)
        return res