class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # for j in range(len(nums)):
            #     if i != j:
            #         if nums[i]+nums[j] == target:
            #             return [i,j]
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                return [min(i, nums.index(diff)), max(i, nums.index(diff))]
        return [-1,-1]
        