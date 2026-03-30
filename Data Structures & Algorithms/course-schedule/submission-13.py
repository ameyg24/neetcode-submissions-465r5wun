class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps = {i:[] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            maps[prereq].append(crs)
        print(maps)
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if maps[i] == []:
                return True
            visited.add(i)
            print(visited)
            for el in maps[i]:
                if not dfs(el):
                    return False
            # visited.remove(i)
            maps[i] = []
            return True
            # visited.remove(i)
        for i in range(numCourses):
            visited = set()
            if not dfs(i):
                return False
        return True
            
# 0<-1<-2
# 1<-3
# 3<-2