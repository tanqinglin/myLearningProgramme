class Solution:
    def removeElement(self, nums, val):
        index = k = 0
        while index < len(nums):
            if nums[index] != val:
                nums[k] = nums[index]
                k += 1
            index += 1
        return k

if __name__ == '__main__':
    Test = Solution()
    print(Test.removeElement([0,1,2,2,3,0,4,2], 2))