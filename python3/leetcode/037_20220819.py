import math

class Solution(object):

    def update(self, cal, row, col, val):
        for j in range(len(cal)):
            if (cal[j][0][0] == row or cal[j][0][1] == col or ((cal[j][0][0] >= row - row % 3) and (cal[j][0][0] < math.ceil(row / 3) * 3) and (cal[j][0][1] >= col - col % 3) and (cal[j][0][1] < math.ceil(col / 3) * 3))) and str(val) in cal[j][1]:
                cal[j][1].remove(str(val))
        return cal

    def solveSudoku(self, board):
        
        cal = []
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    s = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    for k in range(9):
                        if board[i][k] != "." and board[i][k] in s:
                            s.remove(board[i][k])
                        if board[k][j] != "." and board[k][j] in s:
                            s.remove(board[k][j])
                        if board[i - i % 3 + k // 3][j - j % 3 + k % 3] != '.' and board[i - i % 3 + k // 3][j - j % 3 + k % 3] in s:
                            s.remove(board[i - i % 3 + k // 3][j - j % 3 + k % 3])
                    cal.append([(i,j), s])
        
        while cal != []:

            control = True

            for i in range(len(cal) - 1, -1, -1):
                if len(cal[i][1]) == 1:
                    row, col, val = cal[i][0][0], cal[i][0][1], int(cal[i][1][0])
                    board[row][col] = str(val)
                    del cal[i]
                    cal = self.update(cal, row, col, val)
                    control = False
        
            if control:
                for i in range(len(cal) - 1, -1, -1):
                    s = set([])
                    for j in range(len(cal) - 1, -1, -1):
                        if i != j and (cal[i][0][0] == cal[j][0][0] or cal[i][0][1] == cal[j][0][1] or (abs(cal[i][0][0] - cal[j][0][0]) // 3 == 0 and abs(cal[i][0][1] - cal[j][0][1]) // 3 == 0)):
                            s |= set(cal[j][1])
                    if s | set(cal[i][1]) != s:        
                        for j in range(len(cal[i][1])):
                            if cal[i][1][j] not in s:
                                row, col, val = cal[i][0][0], cal[i][0][1], int(cal[i][1][j])
                                board[row][col] = str(val)
                                del cal[i]
                                break
        
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