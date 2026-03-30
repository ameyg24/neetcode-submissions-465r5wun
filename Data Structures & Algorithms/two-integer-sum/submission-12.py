from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        # nums = sorted(nums)
        # while left < right:
        #     sum = nums[left] + nums[right]
        #     if sum > target:
        #         right -= 1
        #     elif sum < target:
        #         left += 1
        #     else:
        #         return [left, right]
        maps = defaultdict(list)
        # for index, val in enumerate(nums):
        #     maps[val] = index
        # for index, val in enumerate(nums):
        #     if target - val in nums and index != maps[target - val]:
        #         return [index, maps[target - val]]
        for index, val in enumerate(nums):
            df = target - val
            if df in maps:
                return [maps[df], index]
            maps[val] = index