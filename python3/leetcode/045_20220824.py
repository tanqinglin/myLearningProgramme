class Solution:
    def jump(self, nums):
        if nums ==[]:
            return -1
        list = [100000] * len(nums)
        list[-1] = 0
        i = len(nums) - 1
        while i > 0:
            i -= 1
            if nums[i] > 0:
                list[i] = min(list[i+1: min(i+1+nums[i], len(nums))]) + 1
        return list[0]

if __name__ == "__main__":
    Test = Solution()
    print(Test.jump([2,3,0,1,4]))