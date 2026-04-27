class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        res = []
        prereqs = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            prereqs[b].append(a)
            indegree[a] += 1
        zeros = []
        for i in range(numCourses):
            if indegree[i] == 0:
                zeros.append(i)
        q = collections.deque(zeros)
        visited = set()
        while q:
            tmp = q.popleft()
            if tmp in visited:
                return []
            visited.add(tmp)
            res.append(tmp)
            for el in prereqs[tmp]:
                indegree[el] -= 1
                if indegree[el] == 0:
                    q.append(el)
        return res if len(res) == numCourses else []