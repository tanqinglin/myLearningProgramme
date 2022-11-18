class Solution:
    def searchMatrix(self, matrix, target):
        i = 0
        while i+1 < len(matrix) and matrix[i+1][0] <= target:
            i += 1
        for n in matrix[i]:
            if n == target:
                return True
            elif n > target:
                break
        return False

if __name__ == "__main__":
    Test = Solution()
    print(Test.searchMatrix(matrix = [[1],[3]], target = 3))