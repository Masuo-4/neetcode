from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        grid_dict = defaultdict(lambda: defaultdict(set))
        
        for row_index, row in enumerate(board):
            for col_index, num in enumerate(row):
                if num == ".": continue
                if (num in row_dict[row_index]\
                    or num in col_dict[col_index]\
                    or num in grid_dict[row_index // 3][col_index // 3]):
                    return False
                else:
                    row_dict[row_index].add(num)
                    col_dict[col_index].add(num)
                    grid_dict[row_index // 3][col_index // 3].add(num)
        
        return True
                
