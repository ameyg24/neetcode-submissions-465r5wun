class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        def dist(a):
            return (a[0]**2+a[1]**2)**0.5
        for p in points:
            d = dist(p)
            ans.append((d,p))
        ans.sort()
        an = []
        for i in range(k):
            an.append(ans[i][1])
        return an

        
        