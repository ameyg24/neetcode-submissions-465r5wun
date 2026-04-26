class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        mapped = {i : [] for i in range(numCourses)}
        print(mapped)
        for a,b in prerequisites:
            indegree[a] += 1
            mapped[b].append(a)
        curr = []
        for i in range(numCourses):
            if indegree[i] == 0:
                curr.append(i)
        q = collections.deque(curr)
        print(mapped, indegree, curr)
        while q:
            tmp = q.popleft()
            for el in mapped[tmp]:
                indegree[el] -= 1
                if indegree[el] == 0:
                    q.append(el)
        return indegree == [0] * numCourses
# 0->1 1->0
# indegree = [1, 1]