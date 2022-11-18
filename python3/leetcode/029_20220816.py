# -*- coding:utf-8 -*-

class Solution:
    def divide(self, dividend, divisor):
        if divisor == 0:
            return False
        sign = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if sign:
            res = -res
        return min(max(-2147483648, res), 2147483647)

if __name__ == '__main__':
    Test = Solution()
    print(Test.divide(12, 3))