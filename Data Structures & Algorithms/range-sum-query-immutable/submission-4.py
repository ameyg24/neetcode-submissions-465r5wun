class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0] * (len(nums) + 1)
        self.prefix[1] = nums[0]
        for i in range(2, len(nums)+ 1):
            self.prefix[i] = self.nums[i-1] +  self.prefix[i-1]
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)