class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Row, Col = len(matrix), len(matrix[0])
        Row_L, Row_R = 0, Row - 1
        ans = -1
        while Row_L <= Row_R:
            # if Row_L == Row_R:
            #     ans = Row_L
            mid_row = (Row_L + Row_R)//2
            if target >= matrix[mid_row][0]:
                Row_L = mid_row + 1
            else:
                Row_R = mid_row - 1
        ans = Row_L - 1
        if ans < 0 :
            return False
        Col_L, Col_R = 0, Col - 1
        while Col_L <= Col_R:
            mid_col = (Col_L + Col_R)//2
            if target > matrix[ans][mid_col]:
                Col_L = mid_col + 1
            elif target < matrix[ans][mid_col]:
                Col_R = mid_col - 1
            else:
                return True
        return False