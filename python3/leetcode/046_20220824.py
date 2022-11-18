class Solution:
    
    def formulate(self, nums, l):
        if l == 0:
            self.result.append(list(self.var))
        else:
            for i in range(l):
                self.var.append(nums[i])
                self.formulate(nums[:i] + nums[i+1:], l - 1)
                self.var.pop()

    
    def permute(self, nums):
        nums.sort()
        self.result = []
        self.var = []
        l = len(nums)
        if l == 0 or l == 1:
            return [nums]
        self.formulate(nums, l)
        return self.result

if __name__ == "__main__":
    Test = Solution()
    print(Test.permute([3,3,0,3]))