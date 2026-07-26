class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = defaultdict(int)
        for i in range(len(s)):
            ends[s[i]] = i
        print(ends)
        size = 0
        end = 0
        res = []
        for r in range(len(s)):
            size += 1
            end = max(end, ends[s[r]])
            if r == end:
                res.append(size)
                size = 0
        return res
