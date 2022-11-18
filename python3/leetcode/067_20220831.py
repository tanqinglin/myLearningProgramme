class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "" or b == "":
            return a + b
        i, d, c  = -1, 0, ""
        while -i <= len(a) and -i <= len(b):
            c, d = str((int(a[i]) + int(b[i]) + d) % 2) + c, (int(a[i]) + int(b[i]) + d) // 2
            i -= 1
        while -i <= len(a):
            c, d = str((int(a[i]) + d) % 2) + c, (int(a[i]) + d) // 2
            i -= 1
        while -i <= len(b):
            c, d = str((int(b[i]) + d) % 2) + c, (int(b[i]) + d) // 2
            i -= 1
        if d:
            c = "1" + c
        return c

if __name__ == "__main__":
    Test = Solution()
    print(Test.addBinary("1010", "1011"))