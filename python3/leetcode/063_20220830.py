class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        matrix = [[0] * n for _ in range(m)]
        matrix[-1][-1] = 1
        for i in range(m-1, -1, -1):
            if obstacleGrid[i][-1] != 1:
                matrix[i][-1] = 1
            else:
                break
        for i in range(n-1, -1, -1):
            if obstacleGrid[-1][i] != 1:
                matrix[-1][i] = 1
            else:
                break
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if not obstacleGrid[i][j]:
                    matrix[i][j] = matrix[i][j+1] + matrix[i+1][j]
        return matrix[0][0]

if __name__ == "__main__":
    Test = Solution()
    print(Test.uniquePathsWithObstacles([[0,1],[0,0]]))