class Solution:
    
    def placeQueen(self, n, rowList, colList):
        
        if len(rowList) == n:
            self.op += 1
        
        if rowList == []:
            startLine = 0
        else:
            startLine = rowList[-1] + 1

        for i in range(startLine, n):
            for j in range(n):
                if j not in colList:
                    attack = 0
                    for k in range(len(rowList)):
                        if abs(rowList[k] - i) == abs(colList[k] - j):
                            attack = 1
                            break
                    if not attack:
                        rowList.append(i)
                        colList.append(j)
                        self.placeQueen(n, rowList, colList)
                        rowList.pop()
                        colList.pop()
    
    def solveNQueens(self, n: int):
        self.op = 0
        self.placeQueen(n, [], [])
        return self.op

if __name__ == "__main__":
    Test = Solution()
    print(Test.solveNQueens(5))