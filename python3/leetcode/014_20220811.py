# -*- coding:utf-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        l = [len(iterm) for iterm in strs]
        s = strs[l.index(min(l))]
        if s == '':
            return ''
        for i in range(1, len(s) + 1):
            sub = s[:i]
            for j in range(len(strs)):
                if strs[j].find(sub) != 0:
                    return sub[:-1]
        return sub


if __name__ == '__main__':
    Test = Solution()
    print(Test.longestCommonPrefix([""]))
        