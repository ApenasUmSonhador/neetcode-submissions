class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        square = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                box_index = (i // 3) * 3 + (j // 3)
                if board[i][j] in row[i] or board[i][j] in square[box_index] or board[i][j] in col[j]:
                    return False
                col[j].add(board[i][j])
                row[i].add(board[i][j])
                square[box_index].add(board[i][j])
        return True