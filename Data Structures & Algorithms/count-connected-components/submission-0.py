class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = {i: [] for i in range(n)}
        for one, two in edges:
            connected[one].append(two)
            connected[two].append(one)
        count = 0
        print(connected)
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for nei in connected[i]:
                dfs(nei)
            return
        # dfs(0)
        # print(visited)
        for i in range(n):
            if i not in visited:
                dfs(i)
                print(visited)
                count += 1
        return count
