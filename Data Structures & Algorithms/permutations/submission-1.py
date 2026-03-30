class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        idx = 0
        while idx < len(nums):
            arr = []
            for r in res:
                x = r.copy()
                for i in range(len(r) + 1):
                    r.insert(i, nums[idx])
                    arr.append(r)
                    # print(arr)
                    # r.pop(i)
                    r = x.copy()
                    print(r)
            res = arr
            idx += 1

        # res = [[1]]
        # r = [1]
        # i = 0: r = [2, 1]
        # i = 1: r = [1, 2]
        return res
