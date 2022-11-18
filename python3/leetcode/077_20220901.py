class Solution:
    
    def formulate(self, list, k):
        if k == 0:
            temp = [i for i in self.var]
            self.result.append(temp)
        else:
            for i in range(len(list)):
                self.var.append(list[i])
                self.formulate(list[i+1:], k - 1)
                self.var.pop()

    def combine(self, n: int, k: int):
        self.result = []
        self.var = []
        if k == 0:
            return []
        self.formulate(list(range(1,n+1)), k)
        return self.result

if __name__ == "__main__":
    Test = Solution()
    print(Test.combine(4, 2))