# -*- coding:utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        maxLen = 1
        maxStr = s[0]
        for i in range(len(s) - 1):
            s1 = self.findPalindrome(s, i, i)
            s2 = self.findPalindrome(s, i, i+1)
            if len(s1) > maxLen:
                maxLen = len(s1)
                maxStr = s1
            if len(s2) > maxLen:
                maxLen = len(s2)
                maxStr = s2
        return maxStr
    
    def findPalindrome(self, s, l, r):
        length = len(s)
        if s[l] != s[r]:
            return ''
        else:
            while l > 0 and r < length - 1 and s[l-1] == s[r+1] :
                l -= 1
                r += 1
            return s[l:r+1]


if __name__ == '__main__':
    Test = Solution()
    print(Test.longestPalindrome('cbbd'))