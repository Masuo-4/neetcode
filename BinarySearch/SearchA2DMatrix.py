class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        
        t, b = 0, len(matrix) - 1
        # t<bだと1ループ減らせる
        while t <= b:
            m = t + (b - t) // 2
            if target < matrix[m][0]:
                b = m - 1 
            elif matrix[m][-1] < target:
                t = m + 1
            else:
                row_num = m
                break
    
        row_num = (t + b) //2
        l, r = 0, len(matrix[row_num]) - 1
        row = matrix[row_num]
        while l <= r:
            m = l + (r - l) // 2
            if target == row[m]:
                return True
            elif target < row[m]:
                r = m - 1
            elif row[m] < target:
                l = m + 1
        return False
        