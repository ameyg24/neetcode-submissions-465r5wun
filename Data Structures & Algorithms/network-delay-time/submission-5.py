import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i : [] for i in range(1, n + 1)}
        for start, end, time in times:
            edges[start].append((end, time))
        minheap = []
        minheap.append((0,k))
        dictionary = {}
        cost = 0
        while minheap:
            dist, node = heapq.heappop(minheap)
            if node not in dictionary:
                print(dist, node)
                cost = dist
                dictionary[node] = dist
                for end, time in edges[node]:
                    if end not in dictionary:
                        heapq.heappush(minheap, (time + dist, end))
        return cost if len(dictionary) == n else -1