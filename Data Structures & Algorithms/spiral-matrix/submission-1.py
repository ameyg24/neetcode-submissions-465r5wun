class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        nr, nc = 0, 0
        # [1,2,3]
        # [4,5,6]
        # [7,8,9]
        row, col = len(matrix), len(matrix[0])
        visited.add((nr,nc))
        output = []
        output.append(matrix[nr][nc])
        while len(output) != row*col:
            for dr, dc in directions:
                nr, nc = nr + dr, nc + dc
                while nr in range(row) and nc in range(col) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    output.append(matrix[nr][nc])
                    print(nr,nc)
                    nr, nc = nr + dr, nc + dc

                print("break")
                nr, nc = nr - dr, nc - dc

        return output
            