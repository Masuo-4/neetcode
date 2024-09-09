class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        for row in matrix:
            l, r = 0, len(row) - 1
            while l <= r:
                m = l + (r - l) // 2
                if target == row[m]:
                    return True
                elif target < row[m]:
                    r = m - 1
                elif row[m] < target:
                    l = m + 1
        return False
    