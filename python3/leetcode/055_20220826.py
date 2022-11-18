class Solution:
    def canJump(self, nums):
        if len(nums) < 2:
            return True
        i, reach = 0, nums[0]
        while i <= reach:
            r = i + nums[i]
            if r >= len(nums) - 1:
                return True
            else:
                reach = max(reach, r)
            if i == reach:
                return False
            i += 1
                

if __name__ == "__main__":
    Test = Solution()
    print(Test.canJump([2,3,1,1,4]))