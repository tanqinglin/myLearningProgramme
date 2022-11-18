class Solution:
    def plusOne(self, digits):
        l = len(digits) - 1
        digits[l] += 1
        while l > 0 and digits[l] > 9:
            digits[l] = 0
            digits[l-1] += 1
            l -= 1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits

if __name__ == "__main__":
    Test = Solution()
    print(Test.plusOne([1,2,3]))