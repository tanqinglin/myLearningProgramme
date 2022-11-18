class Solution:
    def sortColors(self, nums) -> None:
        if len(nums) < 2:
            return nums
        i = left = 0
        while i <= 2:
            right = len(nums) - 1
            while left <= right:
                while left <= right and nums[left] == i:
                    left += 1
                while left <= right and nums[right] != i:
                    right -= 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
            i += 1

if __name__ == "__main__":
    Test = Solution()
    print(Test.sortColors([2,0,1]))