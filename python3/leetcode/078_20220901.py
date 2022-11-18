class Solution:
    def subsets(self, nums):
        global all
        all = []
        self.ans(nums, [])
        return all
    
    def ans(self, nums, n):
        if nums == []:
            all.append(list(n))
        else:
            self.ans(nums[1:], n)
            n += nums[:1]
            self.ans(nums[1:], n)
            n.pop()

if __name__ == "__main__":
    Test = Solution()
    print(Test.subsets([1,2,3]))