class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = "1"
        while n > 1:
            char, sNew, count = "", "", 0
            for i in range(len(s)):
                if s[i] != char:
                    if count != 0:
                        sNew += str(count) + str(char)
                    char = s[i]
                    count = 1
                else:
                    count += 1
            if count != 0:
                sNew += str(count) + str(char)
            n -= 1
            s = sNew
        return s

if __name__ == "__main__":
    Test = Solution()
    print(Test.countAndSay(8))