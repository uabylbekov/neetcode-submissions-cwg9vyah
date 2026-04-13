class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_n = len(matrix)
        col_n = len(matrix[0])
        l = 0
        r = row_n * col_n - 1

        while l <= r:
            m = (r+l) // 2
            row = m // col_n
            col = m % col_n

            if target == matrix[row][col]:
                return True
            
            elif target < matrix[row][col]:
                r = m - 1
            
            else:
                l = m + 1

        return False 