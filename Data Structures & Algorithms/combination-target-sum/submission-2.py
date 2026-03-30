class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        def func(i, currsum):
            if currsum >= target or i >= len(nums):
                if currsum == target:
                    if arr not in res:
                        res.append(arr.copy())
                    return
                else:
                    return
            arr.append(nums[i])
            func(i, currsum + nums[i])
            # if i + 1 < len(nums):
            func(i+1, currsum + nums[i])
            arr.pop()
            func(i+1, currsum)
        func(0, 0)
        return res
            