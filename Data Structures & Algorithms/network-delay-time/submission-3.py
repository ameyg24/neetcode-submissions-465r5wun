import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minheap = []
        minheap.append((0,k))
        dictionary = {}
        while minheap:
            dist, node = heapq.heappop(minheap)
            if node not in dictionary:
                print(dist, node)
                dictionary[node] = dist
                for src, tar, time in times:
                    if src == node:
                        heapq.heappush(minheap, (time + dist, tar))
        return max(dictionary.values()) if len(dictionary) == n else -1