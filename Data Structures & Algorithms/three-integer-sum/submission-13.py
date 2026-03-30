class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i != 0:
                continue
            tmp = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l<r:
                curr = nums[l] + nums[r]
                if curr == tmp:
                    print(i,l,r)
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l+1 in range(n) and  nums[l] == nums[l-1] :
                        l+=1
                    while r in range(n) and nums[r] == nums[r+1] :
                        r-=1
                    # l+=1
                    # r-=1
                elif curr>tmp:
                    r-=1
                else:
                    l+=1
        return res