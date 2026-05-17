class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        n = len(self.nums)
        if left not in range(n) or right not in range(n):
            return -1
        else:
            tmp = 0
            for el in self.nums[left:right + 1]:
                tmp += el
            return tmp


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)