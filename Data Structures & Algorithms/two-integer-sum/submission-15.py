from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = defaultdict(List) # number : idx
        for i, n in enumerate(nums):
            if n in vals:
                vals[n].append(i)
            else:
                vals[n] = [i]
        print(vals)
        for n in nums:
            if target-n in vals:
                if n == target - n:
                    if len(vals[n]) < 2:
                        continue
                    else:
                        return [vals[n][0], vals[n][1]]
                return [vals[n][0], vals[target-n][0]]