class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjlist = collections.defaultdict(set)
        chars = set()
        if len(words) == 1:
            return words[0]
        for i in range(len(words)-1):
            first, second = words[i], words[i+1]
            check = False
            for c1, c2 in zip(first, second):
                chars.add(c1)
                chars.add(c2)
                if c1 != c2 and not check:
                    adjlist[c1].add(c2)
                    check = True
            if not check and len(first) > len(second):
                return ""
        indegree = {a : 0 for a in chars}
        for src, dest in adjlist.items():
            for c in dest:
                indegree[c] += 1
        q = collections.deque()
        for key, value in indegree.items():
            if value == 0:
                q.append(key)
        visit = set()
        res = ""
        print(indegree)
        while q:
            curr = q.popleft()
            visit.add(curr)
            res += curr
            for char in adjlist[curr]:
                if char not in visit:
                    indegree[char] -= 1
                    if indegree[char] == 0:
                        q.append(char)
        return res if len(res) == len(chars) else ""



       

            