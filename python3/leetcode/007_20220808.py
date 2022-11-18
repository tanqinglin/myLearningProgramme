# -*- coding: utf-8 -*-

class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        if x < 0:
            neg = -1
        else:
            neg = 0
        s = str(abs(x))
        s = s[::-1]
        i = 0
        while s[i] == '0':
            i += 1
        s = s[i:]
        if neg:
            result = -int(s)
        else:
            result = int(s)
        if result > 2 ** 31 - 1 or result < - 2 ** 31:
            return 0
        else:
            return result

if __name__ == '__main__':
    Test = Solution()
    print(Test.reverse(-210))