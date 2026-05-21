class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        rev = defaultdict(list)
        for el in nums:
            counter[el] += 1
        print(counter)
        for key, value in counter.items():
            rev[value].append(key)
        print(rev)
        res = []
        for f in range(len(nums), -1, -1):
            if f in rev:
                for el in rev[f]:
                    res.append(el)
            if len(res) == k:
                return res
        return res