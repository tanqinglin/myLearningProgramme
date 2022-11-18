# -*- coding: utf-8 -*-

import numpy as np

class Solution(object):
    def isMatch(self, s, p):
        L = np.zeros((len(p) + 1, len(s) + 1), dtype = bool)
        L[0][0] = True
        for i in range(1, len(p)):
            L[i+1][0] = L[i-1][0] and p[i] == '*'
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i-1] != '*':
                    L[i][j] = L[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == '.')
                else:
                    L[i][j] = L[i-2][j] or L[i-1][j]
                    if p[i-2] == s[j-1] or p[i-2] == '.':
                        L[i][j] = L[i][j-1] or L[i][j]
        return L[-1][-1]

if __name__ == '__main__':
    Test = Solution()
    print(Test.isMatch('ab', '.*'))