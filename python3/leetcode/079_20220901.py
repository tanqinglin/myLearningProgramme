class Solution:
    def exist(self, board, word):
        global rowNum, colNum
        rowNum, colNum = len(board), len(board[0])
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] == word[0]:
                    label = [[1] * colNum for _ in range(rowNum)]
                    label[i][j] = 0
                    if self.travel(board, label, i, j, word[1:]):
                        return True
                    label[i][j] = 1
        return False
    
    def travel(self, board, label, i, j, word):
        if word == "":
            return True
        if i-1 >= 0 and board[i-1][j] == word[0] and label[i-1][j]:
            label[i-1][j] = 0
            if self.travel(board, label, i-1, j, word[1:]):
                return True
            else:
                label[i-1][j] = 1
        if i+1 < rowNum and board[i+1][j] == word[0] and label[i+1][j]:
            label[i+1][j] = 0
            if self.travel(board, label, i+1, j, word[1:]):
                return True
            else:
                label[i+1][j] = 1
        if j-1 >= 0 and board[i][j-1] == word[0] and label[i][j-1]:
            label[i][j-1] = 0
            if self.travel(board, label, i, j-1, word[1:]):
                return True
            else:
                label[i][j-1] = 1
        if j+1 < colNum and board[i][j+1] == word[0] and label[i][j+1]:
            label[i][j+1] = 0
            if self.travel(board, label, i, j+1, word[1:]):
                return True
            else:
                label[i][j+1] = 1
        return False

if __name__ == "__main__":
    Test = Solution()
    print(Test.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))