class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        i = j = 0
        count = 1
        while count <= n ** 2:

            # 1: right
            while count <= n ** 2 and j < n and not matrix[i][j]:
                matrix[i][j] = count
                j += 1
                count += 1

            # 2: down
            j -= 1
            while count <= n ** 2 and i+1 < n and not matrix[i+1][j]:
                i += 1
                matrix[i][j] = count
                count += 1
            
            # 3: left
            j -= 1
            while count <= n ** 2 and j >= 0 and not matrix[i][j]:
                matrix[i][j] = count
                j -= 1
                count += 1

            # 4: up
            j += 1
            while count <= n ** 2 and i-1 >= 0 and not matrix[i-1][j]:
                i -= 1
                matrix[i][j] = count
                count += 1
            j += 1
        
        return matrix

if __name__ == "__main__":
    Test = Solution()
    print(Test.generateMatrix(20))