# -*- coding:utf:8 -*-

# class Solution(object):

#     def zigZagSort(self, L):
#         for i in range(len(L) - 1):
#             for j in range(i + 1, len(L)):
#                 if L[i][0] > L[j][0]:
#                     L[i], L[j] = L[j], L[i]
#                 elif L[i][0] == L[j][0]:
#                     if L[i][1] > L[j][1]:
#                         L[i], L[j] = L[j], L[i]
#         return L

#     def convert(self, s, numRows):
#         S, L = '', []
#         i, l = 0, len(s)
#         row = 0
#         col = 0
#         down= 1
#         while i < l:
#             while down == 1 and i < l:
#                 if row < numRows:
#                     L.append([row, col, s[i]])
#                     row += 1
#                     i += 1
#                 else:
#                     row -= 1
#                     down = 0
#             if numRows >= 3:
#                 while down == 0 and i < l:
#                     row -= 1
#                     col += 1
#                     L.append([row, col, s[i]])
#                     i += 1
#                     if row == 1:
#                         down = 1
#                         row -= 1
#                         col += 1
#             else:
#                 row = 0
#                 col += 1
#                 down = 1
#         # L = self.zigZagSort(L)
#         L.sort(key = lambda x: x[1])
#         L.sort(key = lambda x: x[0])

#         for iterm in L:
#             S += iterm[2]
#         return S



class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

if __name__ == '__main__':
    Test = Solution()
    print(Test.convert('PAYPALISHIRING', 3))