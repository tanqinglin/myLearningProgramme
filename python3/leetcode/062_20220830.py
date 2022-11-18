class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = max(m,n), min(m,n)
        a = b = 1
        while n > 1:
            a *= n - 1
            b *= m
            n -= 1
            m += 1
        return b // a

if __name__ == "__main__":
    Test = Solution()
    print(Test.uniquePaths(3,2))