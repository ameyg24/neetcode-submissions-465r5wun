class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = [[]]
        idx = 0
        while idx < len(nums):
            tmp = []
            for el in stack:
                for i in range(len(el) + 1):

                    x = el.copy()
                    x.insert(i, nums[idx])
                    tmp.append(x)
                    print(tmp)
                    print(x)
            stack = tmp
            idx += 1
        return stack