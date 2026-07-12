class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        columns = {i: set() for i in range(9)}
        squares = {i: set() for i in range(9)}

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != ".":
                    square = (i // 3) * 3 + (j // 3)
                    if num in rows[i] or num in columns[j] or num in squares[square]:
                        return False

                    rows[i].add(num)
                    columns[j].add(num)
                    squares[square].add(num)
        
        return True