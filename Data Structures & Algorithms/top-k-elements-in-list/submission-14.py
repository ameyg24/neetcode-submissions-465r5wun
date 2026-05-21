import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        rev = defaultdict(list)
        for key, value in counter.items():
            rev[value].append(key)
        res = []
        minheap = [-e for e in rev.keys()]
        heapq.heapify(minheap)
        while len(res) < k:
            t = -1*heapq.heappop(minheap)
            for el in rev[t]:
                res.append(el)
        return res
