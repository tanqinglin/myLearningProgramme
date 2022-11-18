# -*- coding: utf-8 -*-

class Solution(object):
    def romanToInt(self, s):
        key = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num, i = 0, 0
        while i < len(s):
            if i + 1 < len(s) and key[s[i+1]] > key[s[i]]:
                num += key[s[i+1]] - key[s[i]]
                i += 1
            else:
                num += key[s[i]]
            i += 1
        return num

if __name__ == '__main__':
    Test = Solution()
    print(Test.romanToInt('MCMXCIV'))

