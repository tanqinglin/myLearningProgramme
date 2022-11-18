# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substring = ''
        length = 0
        max_len = 0
        l = 0
        while l < len(s):
            if substring.find(s[l]) == -1:
                substring += s[l]
                length += 1
            else:
                if length > max_len:
                    max_len = length
                length = length - substring.find(s[l])
                substring = substring[substring.find(s[l]) + 1:] + s[l]
            l += 1
        return max(max_len, length)

if __name__ == '__main__':
    T = Solution()
    print(T.lengthOfLongestSubstring(' '))