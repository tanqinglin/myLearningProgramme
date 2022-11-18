class Solution(object):
    
    def generateParenthesis(self, n):
        
        L = []

        def backtracking(s, l, r):
            if l == r == 0:
                nonlocal L
                L.append(s)
            if l > 0:
                backtracking(s+'(', l-1, r)
            if l < r:
                backtracking(s+')', l, r-1)
        
        backtracking('', n, n)
        return L

if __name__ == '__main__':
    Test = Solution()
    print(Test.generateParenthesis(1))