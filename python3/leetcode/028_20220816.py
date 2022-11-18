class Solution:
    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        if len(haystack) < len(needle):
            return -1
        index = 0
        while index < len(haystack):
            if haystack[index] == needle[0]:
                d = 0
                while d < len(needle) and index + d < len(haystack) and haystack[index + d] == needle[d]:
                    d += 1
                if d == len(needle):
                    return index
            index += 1
        return -1

if __name__ == '__main__':
    Test = Solution()
    print(Test.strStr("hello", "ll"))