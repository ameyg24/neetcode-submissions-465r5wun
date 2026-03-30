from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            arr[value].append(key)
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for num in arr[i]:
                res.append(num)
            if len(res) == k:
                return res

