class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            line_set = set()
            column_set = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in line_set:
                    return False
                line_set.add(board[i][j])

                if board[j][i] != "." and board[j][i] in column_set:
                    return False
                column_set.add(board[j][i])
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_set = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != "." and board[i+k][j+l] in square_set:
                            return False
                        square_set.add(board[i+k][j+l])

        return True