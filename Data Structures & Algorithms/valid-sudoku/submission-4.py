class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for i in range(9)]
        row = [set() for i in range(9)]
        square = [[set() for c in range(3)] for r in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row[i] or board[i][j] in square[i//3][j//3] or board[i][j] in col[j]:
                        return False
                col[j].add(board[i][j])                        
                row[i].add(board[i][j])                        
                square[i//3][j//3].add(board[i][j])                        
        return True