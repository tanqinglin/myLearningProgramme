class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range(m-2, -1, -1):
            grid[i][-1] += grid[i+1][-1]
        for i in range(n-2, -1, -1):
            grid[-1][i] += grid[-1][i+1]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        return grid[0][0]

if __name__ == "__main__":
    Test = Solution()
    print(Test.minPathSum([[1,2,3],[4,5,6]])) 