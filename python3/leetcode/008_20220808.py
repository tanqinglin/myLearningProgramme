# -*- coding: utf-8 -*-

class Solution(object):
    def myAtoi(self, s):
        d = 0

        if s == '':
            return 0
        
        while s[d] == ' ':
            d += 1
            if d == len(s):
                return 0

        if s[d] != '+' and s[d] != '-' and not s[d].isdigit():
            return 0
        
        # 符号
        if s[d] == '+':
            sign = 1
            n = 1
        elif s[d] == '-':
            sign = -1
            n = 1
        else:
            sign = 1
            n = 0
        
        # 数值获取及处理
        l, r = 0, 0
        judge = False
        if not n:
            l = r = d
            judge = True
        elif d + 1 < len(s) and s[d+1].isdigit():
            d += 1
            l = d
            r = d
            judge = True
        while d + 1 < len(s) and s[d+1].isdigit():
            d += 1
            r = d
        if judge and l <= r and r <= len(s):
            num = sign * int(s[l:r+1])
        else:
            num = 0
        if num < -2 ** 31:
            num = -2 ** 31
        if num > 2 ** 31 - 1:
            num = 2 ** 31 - 1
        return num


if __name__ == '__main__':
    Test = Solution()
    print(Test.myAtoi(' '))