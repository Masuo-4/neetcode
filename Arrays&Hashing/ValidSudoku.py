from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dct = defaultdict(set)
        col_dct = defaultdict(set)
        grid_dct = defaultdict(set)
        for row_num, row in enumerate(board):
            for col_num, digit in enumerate(row):
                grid_num = row_num // 3 + (col_num // 3) * 3
                if digit == ".":
                    continue
                else:
                    if digit in row_dct[row_num]\
                        or digit in col_dct[col_num]\
                        or digit in grid_dct[grid_num]:
                            return False
                    else:
                        row_dct[row_num].add(digit)
                        col_dct[col_num].add(digit)
                        grid_dct[grid_num].add(digit)
        
        return True
    