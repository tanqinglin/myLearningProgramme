def quick_sort(nums, l, r): # 快排
    n = nums[l]
    left, right = l, r
    while left < right:
        while nums[right] >= n and left < right:
            right -= 1
        if left < right:
            nums[left] = nums[right]       
        while nums[left] <= n and left < right:
            left += 1
        if left < right:
            nums[right] = nums[left]
    nums[left] = n
    if left > l:
        quick_sort(nums, l, left - 1)
    if right < r:
        quick_sort(nums, right + 1, r)
    return nums

class Solution:

    def nextPermutation(self, nums):
        l = len(nums) - 1
        while l > 0 and nums[l] <= nums[l - 1]:
            l -= 1
        for i in range(len(nums)-1, l-1, -1):
            if nums[i] > nums[l-1]:
                nums[l - 1], nums[i] = nums[i], nums[l-1]
                break
        return quick_sort(nums, l, len(nums)-1)

if __name__ == "__main__":
    Test = Solution()
    print(Test.nextPermutation([5,1,1]))