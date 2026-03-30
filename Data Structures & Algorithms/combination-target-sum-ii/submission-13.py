class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        def func(i, currsum):
            if currsum >= target or i >= len(candidates):
                if currsum == target:
                    tmp = sorted(arr)
                    if tmp not in res:
                        res.append(tmp.copy())
                    return
                else:
                    return
            arr.append(candidates[i])
            func(i+1, currsum + candidates[i])
            arr.pop()
            func(i+1, currsum)
        func(0,0)
        return res