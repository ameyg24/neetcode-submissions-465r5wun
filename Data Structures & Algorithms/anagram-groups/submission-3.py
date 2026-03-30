class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for i, item in enumerate(strs):
            tmp = {}
            for char in item:
                tmp[char] = 1 + tmp.get(char, 0)
            maps[(item, i)] = tmp
        ans = []
        for item in maps:
            res = [item[0]]
            for tmp in maps:
                if item == tmp:
                    continue
                if maps[item] == maps[tmp]:
                    res.append(tmp[0])
            if sorted(res) not in ans: ans.append(sorted(res))
        return ans