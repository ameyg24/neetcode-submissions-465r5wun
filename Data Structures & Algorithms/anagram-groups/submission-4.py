class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = collections.defaultdict(list)
        for el in strs:
            tmp = ''.join(sorted(el))
            maps[tmp].append(el)
        return list(maps.values())
        