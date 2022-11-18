class Solution:
    def rotate(self, A):
        n = len(A)
        for i in range(n//2):
            for j in range(n-n//2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = A[~j][i], A[~i][~j], A[j][~i], A[i][j]
        return A

if __name__ == "__main__":
    Test = Solution()
    print(Test.rotate([[1,2,3],[4,5,6],[7,8,9]]))