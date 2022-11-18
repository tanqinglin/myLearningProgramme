class Solution:
    def solveSudoku(self, board) -> None:
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return
            
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

        dfs(0)
        return board

if __name__ == "__main__":
    Test = Solution()
    board = [[".",".","9","7","4","8",".",".","."],
             ["7",".",".",".",".",".",".",".","."],
             [".","2",".","1",".","9",".",".","."],
             [".",".","7",".",".",".","2","4","."],
             [".","6","4",".","1",".","5","9","."],
             [".","9","8",".",".",".","3",".","."],
             [".",".",".","8",".","3",".","2","."],
             [".",".",".",".",".",".",".",".","6"],
             [".",".",".","2","7","5","9",".","."]]
    print(Test.solveSudoku(board))