class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # -4,-1,-1,0,1,2
        res = []
        for i in range(len(nums)):
            if i-1 in range(len(nums)) and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            tmp = -nums[i]
            while left<right:
                if nums[left]+nums[right] == tmp:
                    res.append([nums[i], nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left]+nums[right] > tmp:
                    right -= 1
                else:
                    left += 1
        return res