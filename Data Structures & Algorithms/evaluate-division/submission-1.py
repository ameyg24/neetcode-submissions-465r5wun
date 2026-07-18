class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(start, end):
            # if start == end:
            #     return 1.0
            if (start or end) not in graph:
                return -1.0
            stack = [(start, 1.0)]
            res = 1.0
            visited = set()
            while stack:
                curr, val = stack.pop()
                if curr == end:
                    return val
                if curr not in visited:
                    visited.add(curr)
                    for nei, tmp in graph[curr]:
                        if nei not in visited:
                            stack.append((nei,tmp * val))
            return -1.0
        
        graph = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            graph[a].append((b, value))
            graph[b].append((a, 1/value))
        
        res = []
        for x, y in queries:
            res.append(dfs(x,y))
        return res