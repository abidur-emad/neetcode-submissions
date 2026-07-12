class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: [] for i in range(9)}
        columns = {i: [] for i in range(9)}
        squares = {i: [] for i in range(9)}

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != ".":
                    rows[i].append(num)
                    columns[j].append(num)
                    squares[(i // 3) * 3 + (j // 3)].append(num)
        
        for groups in (rows, columns, squares):
            for group in groups.values():
                if len(set(group)) < len(group):
                    return False

        return True