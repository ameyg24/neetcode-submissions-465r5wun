class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        idx = 0
        while idx < len(nums):
            arr = []
            for r in res:
                for i in range(len(r) + 1):
                    x = r.copy()
                    x.insert(i, nums[idx])
                    arr.append(x)
            res = arr
            idx += 1

        # res = [[1]]
        # r = [1]
        # i = 0: r = [2, 1]
        # i = 1: r = [1, 2]
        return res
