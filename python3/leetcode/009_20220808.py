# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            L = []
            while x > 0:
                L.append(x % 10)
                x = x // 10
            l, r = 0, len(L) - 1
            while l < r:
                if L[l] != L[r]:
                    return False
                l += 1
                r -= 1
            return True

if __name__ == '__main__':
    Test = Solution()
    print(Test.isPalindrome(10))