class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        mp = {}
        print(nums)
        # for idx, el in enumerate(nums):
        #     mp[]
        res = []
        while i < len(nums):
            while 0 < i and nums[i] == nums[i-1]:
                i += 1
                if i == len(nums):
                    return res
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[r] + nums[l] > target:
                    r -= 1
                elif nums[r] + nums[l] < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
            i += 1
        return res
                
                