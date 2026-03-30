class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        visited = set()
        maps = {i:[] for i in range(n)}
        print(maps)
        for one, two in edges:
            maps[one].append(two)
            maps[two].append(one)
        def dfs(i):
            visited.add(i)
            for el in maps[i]:
                if el not in visited:
                    dfs(el)
        dfs(0)
        return len(visited) == n
# 0
# 0,1,2
# 0,1,4,2