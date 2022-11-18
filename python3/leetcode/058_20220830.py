class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip(" ")
        return len(s.split(" ")[-1])

if __name__ == "__main__":
    Test = Solution()
    print(Test.lengthOfLastWord("luffy is still joyboy"))