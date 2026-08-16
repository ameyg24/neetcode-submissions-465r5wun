from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            tmp = sorted(s)
            tmp = ''.join(tmp)
            res[tmp].append(s)
        return list(res.values())