class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegree = [0] * numCourses
        pres = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[crs] += 1
            pres[pre].append(crs)
        q = collections.deque()
        print(indegree)
        print(pres)
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        total = 0
        while q:
            node = q.popleft()
            total += 1
            res.append(node)
            for nei in pres[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if total == numCourses else []
