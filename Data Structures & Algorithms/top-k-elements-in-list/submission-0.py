class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HashMap = {}
        for el in nums:
            HashMap[el] = 1 + HashMap.get(el, 0)
        lst = []
        for key, value in HashMap.items():
            lst.append([value, key])
        lst.sort()
        # res = []
        # for i in range(k):
        #     res.append(lst.pop()[1])
        res = []
        for i in range(1,k + 1):
            res.append(lst[-i][1])
        return res
