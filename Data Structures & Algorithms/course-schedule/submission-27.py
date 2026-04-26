class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapped = {i : [] for i in range(numCourses)}
        for a,b in prerequisites:
            mapped[b].append(a)
        def dfs(i, visited):
            if i in visited:
                return False
            visited.add(i)
            for el in mapped[i]:
                if not dfs(el, visited):
                    return False
            visited.remove(i)
            return True
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True
