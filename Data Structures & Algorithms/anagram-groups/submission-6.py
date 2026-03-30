from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for el in strs:
            tmp = sorted(el)
            tmp = "".join(tmp)
            print(tmp)
            maps[tmp].append(el)
        x = maps.values()
        return list(x)