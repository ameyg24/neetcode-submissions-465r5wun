class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        print(cnt)
        # maps = {}
        maxs = -1
        for key, value in cnt.items():
            if key == value:
                maxs = max(key, maxs)
        return maxs