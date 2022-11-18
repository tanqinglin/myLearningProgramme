class Solution(object):
    def isValid(self, s):
        
        dict = {')': '(', ']': '[', '}': '{'}

        if s == '':
            return True

        i, j, stack = 0, 0, []
        while i < len(s):
            stack.append(s[i])
            i += 1
            j += 1 # stack.length + 1
            while j - 1 >= 0 and stack[j - 1] in dict:
                if j - 2 >= 0 and stack[j - 2] == dict[stack[j - 1]]:
                    stack.pop()
                    stack.pop()
                    j -= 2
                else:
                    return False
        if stack == []:
            return True
        else:
            return False


if __name__ == '__main__':
    Test = Solution()
    print(Test.isValid('()[]{}'))