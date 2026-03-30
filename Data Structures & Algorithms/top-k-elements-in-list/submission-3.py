class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for el in nums:
            maps[el] = 1 + maps.get(el, 0)
        print(maps)
        tmp = []
        for key, value in maps.items():
            tmp.append([value, key])
        tmp.sort(reverse=True)
        print(tmp)
        ans=[]
        for i in range(k):
            ans.append(tmp[i][1])
        return ans