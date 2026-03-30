class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 0
        
        for i in range(len(nums)):
            arr = nums[:]
            tmp = 1
            init = nums[i]
            for j in range(len(nums)):
                if (init + 1) in arr:
                    tmp += 1
                    arr.remove(init + 1)
                    init += 1
            if tmp > maxi:
                maxi = tmp
        return maxi
            # for j in range(len(nums)):
            #     if i == j:
            #         continue
            #     if nums[j] + 1 == tmp[-1]: