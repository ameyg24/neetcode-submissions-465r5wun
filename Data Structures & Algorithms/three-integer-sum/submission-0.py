class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        maps = {}
        for index, el in enumerate(nums):
            maps[el] = index
        ans = []
        for i in range(len(nums)):
            diff = 0 - nums[i]
            for j in range(len(nums)):
                if i == j:
                    continue
                second_diff = diff - nums[j]
                if second_diff in nums and j != maps[second_diff] != i:
                    if sorted([nums[i],nums[j],second_diff]) not in ans: ans.append(sorted([nums[i],nums[j],second_diff]))
        return ans
