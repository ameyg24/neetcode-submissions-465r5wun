class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for i, item in enumerate(strs):        # add index
            tmp = {}
            for char in item:
                tmp[char] = 1 + tmp.get(char, 0)
            maps[(i, item)] = tmp              # use (index, string) as key
        ans = []
        for item in maps:
            res = [item[1]]                    # item[1] = the string itself
            for tmp in maps:
                if item == tmp:
                    continue
                if maps[item] == maps[tmp]:
                    res.append(tmp[1])
            if sorted(res) not in ans:
                ans.append(sorted(res))
        return ans
