class Solution:
    
    def getPermutation(self, n: int, k: int) -> str:
        
        label = [1] * n # when label[i] = 1, it labels number i+1 is unused
        i, j = n - 1, 1
        
        while i > 0:
            j *= i
            i -= 1
        c, k, s = n-1, k-1, ""

        while k > 0:
            count = k // j
            for i in range(n):
                if label[i]:
                    if count > 0:
                        count -= 1
                    else:
                        label[i] = 0
                        s += str(i+1)
                        break
            k %= j                                   
            j //= c
            c -= 1

        for i in range(n):
            if label[i]:
                s += str(i+1)
        
        return s

if __name__ == "__main__":
    Test = Solution()
    print(Test.getPermutation(9, 7))