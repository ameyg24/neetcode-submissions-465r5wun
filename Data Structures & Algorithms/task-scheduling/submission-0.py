import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        maxheap = [-c for c in counts.values()]
        heapq.heapify(maxheap)
        print(maxheap)
        q = collections.deque()
        time = 0
        while q or maxheap:
            time += 1
            if maxheap:
                tmp = 1 + heapq.heappop(maxheap)
                if tmp < 0:
                    q.append([tmp, time + n])
            if q and q[0][1] == time:
                val, t = q.popleft()
                heapq.heappush(maxheap, val)
        return time