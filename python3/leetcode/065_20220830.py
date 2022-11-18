class Solution:
    def isNumber(self, s: str) -> bool:
        d = {"sign": 0, "e": 0, ".": 0}
        i = 0
        while i < len(s):
            if s[i] == "+" or s[i] == "-":
                if d["sign"] == 0:
                    d["sign"] = 1
                    if (i+1 >= len(s) or (not s[i+1].isdigit() and s[i+1] != ".")):
                        return False
                else:
                    return False

            elif s[i] == ".":
                if d["."] == 0:
                    d["."] = 1
                    d["sign"] = 1
                    if (i+1 >= len(s) or (s[i+1] != '+' and s[i+1] != '-' and s[i+1] != 'e' and s[i+1]!= 'E' and not s[i+1].isdigit())) and (i-1 < 0 or not s[i-1].isdigit()):
                        return False
                else:
                    return False

            elif s[i] == "E" or s[i] == "e":
                if d["e"] == 0:
                    d["e"] = d["."] = 1
                    d["sign"] = 0
                    if i+1 >= len(s) or (s[i+1] != '+' and s[i+1] != '-' and not s[i+1].isdigit()) or i-1 < 0 or (s[i-1] != '+' and s[i-1] != '-' and s[i-1] != '.' and not s[i-1].isdigit()):
                        return False
                else:
                    return False

            elif s[i].isdigit():
                d["sign"] = 1
                while i + 1 < len(s) and s[i+1].isdigit():
                    i += 1
            
            else:
                return False

            i += 1
        return True

if __name__ == "__main__":
    Test = Solution()
    print(Test.isNumber("46.e4"))