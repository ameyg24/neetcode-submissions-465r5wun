from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        ans = defaultdict(list)
        for key, value in counts.items():
            ans[value].append(key)
        res = []
        for freq in range(len(nums),0,-1):
            if freq in ans:
                for el in ans[freq]:
                    res.append(el)
            if len(res) == k:
                return res
        return res