import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            print(heap)
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x == y:
                continue
            else:
                heapq.heappush(heap, -abs(x-y))
                print(heap)
        if heap:
            return heap[0] if heap[0] > 0 else -1*heap[0]
        return 0
