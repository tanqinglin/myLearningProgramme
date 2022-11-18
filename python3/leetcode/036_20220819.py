class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            rowSet, colSet, squareSet = [], [], []
            for j in range(9):
                if board[i][j] != "." and board[i][j] in rowSet:
                    return False
                else:
                    rowSet.append(board[i][j])
                if board[j][i] != "." and board[j][i] in colSet:
                    return False
                else:
                    colSet.append(board[j][i])
                s = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
                if s != '.' and s in squareSet:
                    return False
                else:
                    squareSet.append(board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3])
        return True

if __name__ == "__main__":
    Test = Solution()

    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    print(Test.isValidSudoku(board))