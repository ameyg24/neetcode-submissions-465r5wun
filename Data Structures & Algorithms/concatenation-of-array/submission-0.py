class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = 2*len(nums)
        newArr = [0] * length
        for i in range(len(nums)):
            newArr[i] = nums[i]
            newArr[i + len(nums)] = nums[i]
        # for i in range(self.length, self.capacity):
        #     newArr[i] = newArr[i - self.length]
        return newArr
