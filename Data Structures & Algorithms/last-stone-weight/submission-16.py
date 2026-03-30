import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        array = [-x for x in stones]
        heapq.heapify(array)
        while len(array) > 1:
            x = -heapq.heappop(array)
            y = -heapq.heappop(array)
            if x == y:
                continue
            else:
                heapq.heappush(array, y-x)
        return -array[0] if array else 0