import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        t = len(nums) - k
        print(t)
        while t > 0:
            heapq.heappop(nums)
            t-=1
        return heapq.heappop(nums)