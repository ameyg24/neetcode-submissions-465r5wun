class Solution:
    def rob(self, nums: List[int]) -> int:
        
        first = 0
        second = 0
        rob1, rob2 = 0,0
        n = len(nums)
        if n ==1: return nums[0]
        for i in range(n-1):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        first = rob2
        rob1, rob2 = 0,0
        for i in range(1, n):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        second = rob2
        return max(first, second)