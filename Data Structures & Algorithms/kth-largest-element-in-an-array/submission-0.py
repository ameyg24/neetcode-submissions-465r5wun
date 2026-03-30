class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for el in nums:
            heapq.heappush(heap, el)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]