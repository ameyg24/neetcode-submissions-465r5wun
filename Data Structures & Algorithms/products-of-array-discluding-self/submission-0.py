class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [0]* len(nums)
        product = 1
        for el in nums:
            product *= el
        for i in range(len(nums)):
            if nums[i] != 0:
                arr[i] = product//nums[i]
            else:
                tmp = 1
                for j in range(len(nums)):
                    if j != i:
                        tmp *= nums[j]
                arr[i] = tmp
        return arr
