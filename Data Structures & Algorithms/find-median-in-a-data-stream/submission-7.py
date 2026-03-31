import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if len(self.maxheap) == len(self.minheap):
            if self.maxheap and self.minheap and num >= self.minheap[0]:
                tmp = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -tmp)
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)
        else:
            if self.maxheap and num < -self.maxheap[0]:
                tmp = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, tmp)
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)

    def findMedian(self) -> float:
        print(self.maxheap, self.minheap)
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0]+self.minheap[0])/2
        
        