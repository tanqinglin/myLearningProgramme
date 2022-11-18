class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        match[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                match[i][0] = True
            else:
                break
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == "?":
                    match[i][j] = match[i-1][j-1]
                elif p[i - 1] == "*":
                    match[i][j] = match[i-1][j] or match[i][j-1]
                else:
                    match[i][j] = match[i-1][j-1] and (p[i - 1] == s[j - 1])
        return match[-1][-1]

if __name__ == "__main__":
    Test = Solution()
    print(Test.isMatch("aa", "*"))