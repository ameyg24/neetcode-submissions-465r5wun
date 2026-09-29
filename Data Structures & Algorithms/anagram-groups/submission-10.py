from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)

        for string in strs:
            t = "".join(sorted(string))
            maps[t].append(string)

        return [value for key,value in maps.items()]