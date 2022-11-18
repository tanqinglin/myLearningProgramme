class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        list1 = [0] * len(num1)
        list2 = [0] * len(num2)
        list3 = [0] * (len(num1) + len(num2))
        
        index = 0
        while index < len(num1):
            list1[index] = int(num1[len(num1) - index - 1])
            index += 1
        
        index = 0
        while index < len(num2):
            list2[index] = int(num2[len(num2) - index - 1])
            index += 1
        
        i = 0
        while i < len(num1):
            j = 0
            while j < len(num2):
                list3[i+j] += list1[i] * list2[j]
                j += 1
            i += 1
        
        i, s = 0, ""
        while i < len(list3) - 1:
            list3[i+1] += list3[i] // 10
            s = str(list3[i] % 10) + s
            i += 1
        s = str(list3[i] % 10) + s
        
        j = 0
        while j < len(s) - 1 and s[j] == "0":
            j += 1
        
        return s[j:]

if __name__ == "__main__":
    Test = Solution()
    print(Test.multiply("1111111111111111111", "111111111111111111"))