class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square_set = [[set() for x in range(3)] for y in range(3)]
        for i in range(9):
            line_set = set()
            column_set = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in line_set or board[i][j] in square_set[i//3][j//3]:
                        return False                
                    line_set.add(board[i][j])
                    square_set[i//3][j//3].add(board[i][j])

                if board[j][i] != "." and board[j][i] in column_set:
                    return False
                column_set.add(board[j][i])
        return True