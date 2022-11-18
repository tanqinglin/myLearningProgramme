class Solution:
    def mySqrt(self, x: int) -> int:
        return self.fb(0, x, x)

    def fb(self, s, e, x):
        d = (s + e) // 2
        if d ** 2 <= x and (d+1) ** 2 > x:
            return d
        elif d ** 2 < x:
            return self.fb(d+1, e, x)
        else:
            return self.fb(s, d-1, x)

if __name__ == "__main__":
    Test = Solution()
    print(Test.mySqrt(x = 0))