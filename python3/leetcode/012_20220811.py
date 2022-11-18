# -*- coding: utf-8 -*-

class Solution(object):
    
    def intToRoman(self, num):
        key = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        s, d = key[1000] * (num // 1000) + '', 1000
        num %= d
        while num > 0:
            d //= 10
            if num // d != 0:
                if num // d == 9 or num // d == 4:
                    s += key[d] + key[d * (num // d + 1)]
                elif num // d > 4:
                    s += key[5 * d] + key[d] * (num // d - 5)
                else:
                    s += key[d] * (num // d)
            num %= d
        return s



if __name__ == '__main__':
    Test = Solution()
    print(Test.intToRoman(1994))