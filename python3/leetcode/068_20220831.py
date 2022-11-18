class Solution:
    def fullJustify(self, words, maxWidth):
        space = [0] * len(words)
        i = l = num = 0
        
        while i < len(words):
            if l + len(words[i]) + max(num, 0) <= maxWidth:
                l += len(words[i])
                num += 1
                i += 1
            else:
                if num == 1:
                    space[i-1] = maxWidth - l
                else:
                    space[i-1] = 0
                m = maxWidth - l
                for j in range(i-2, i - num - 1, -1):
                    num -= 1
                    space[j] = m // num
                    m -= space[j]
                l = num = 0
        space[i-1] = maxWidth - l - (num-1)
        for j in range(i-2, i - num - 1, -1):
            space[j] = 1

        # print
        i = m = 0
        list = []
        while i < len(words):
            s = ""
            while i < len(words) and len(s + words[i] + " " * space[i]) <= maxWidth:
                s += words[i] + " " * space[i]
                i += 1
            list.append(s)
        return list

if __name__ == "__main__":
    Test = Solution()
    print(Test.fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))