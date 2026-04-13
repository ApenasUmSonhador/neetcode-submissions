class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            count_l = {}
            count_c = {}
            for j in range(9):
                if board[i][j] != "." and count_l.get(board[i][j], False):
                    return False
                count_l[board[i][j]] = True

                if board[j][i] != "." and count_c.get(board[j][i], False):
                    return False
                count_c[board[j][i]] = True
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                count = {}
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != "." and count.get(board[i+k][j+l], False):
                            print(i+k, j+l, count)
                            return False
                        count[board[i+k][j+l]] = True

        return True