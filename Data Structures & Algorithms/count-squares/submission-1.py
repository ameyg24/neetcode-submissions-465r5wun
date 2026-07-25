from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        res = 0
        for nx, ny in self.points:
            if abs(nx-x) != abs(ny-y) or (x==nx and y == ny):
                continue
            if (x,ny) in self.points and (nx,y) in self.points:
                res += self.points[(nx,ny)]*self.points[(x,ny)]*self.points[(nx,y)]
        return res
        
