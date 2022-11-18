class Solution:
    def longestValidParentheses(self, s):
        l,r = 0, len(s) - 1
        while l < len(s) and s[l] == ')':
            l += 1
        while r >= 0 and s[r] == '(':
            r -= 1
        s = s[l:r+1]
        
        if s == "":
            return 0
        
        label = [0]*len(s)
        l, count, stack = 0, -1, []
        while l < len(s):
            if s[l] == "(":
                count += 1
                if len(stack) < count + 1:
                   stack.append(l)
                else:
                    stack[count] = l
            else:
                if count >= 0:
                    label[stack[count]] = label[l] = 1
                    count -= 1
            l += 1
        
        part = m = 0
        for i in range(len(s)):
            if label[i] == 1:
                part += 1
            else:
                if part > m:
                    m = part
                part = 0
        return max(m, part)


        # num = con = result = 0
        # substring = ''
        # l = has_con = count = 0
        # while l < len(s):
        #     if s[l] == "(":
        #         substring += s[l]
        #         if has_con:
        #             count += 1
        #     else:
        #         if len(substring) > 0:
        #             num += 2
        #             substring = substring[:-1]
        #             if substring == "":
        #                 con += num
        #                 num = 0
        #                 has_con = 1
        #                 if con > result:
        #                     result = con
        #         else:
        #             if num > result:
        #                 result = num
        #             num = con = 0
        #             substring = ""
        #     l += 1
        # return max(result, num)

if __name__ == "__main__":
    Test = Solution()
    print(Test.longestValidParentheses(""))