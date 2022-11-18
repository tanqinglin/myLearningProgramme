class Solution:
    def removeDuplicates(self, nums):
        if nums == []:
            return 0
        d, k = nums[0], 0
        index = 1
        while index < len(nums):
            if nums[index] != d:
                k = k + 1
                nums[k] = d = nums[index]
            index += 1
        return k+1

if __name__ == '__main__':
    Test = Solution()
    print(Test.removeDuplicates([1,2,2,3,3,4]))