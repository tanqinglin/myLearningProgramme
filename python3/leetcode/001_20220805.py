# -*- coding: utf-8 -*-

def quick_sort(nums, l, r): # 快排
        n = nums[l]
        left, right = l, r
        while left < right:
            while nums[right][1] >= n[1] and left < right:
                right -= 1
            if left < right:
                nums[left] = nums[right]       
            while nums[left][1] <= n[1] and left < right:
                left += 1
            if left < right:
                nums[right] = nums[left]
        nums[left] = n
        if left > l:
            quick_sort(nums, l, left - 1)
        if right < r:
            quick_sort(nums, right + 1, r)
        return nums

class Solution(object):

    def twoSum(self, nums, target):
        nums_sorted = quick_sort(list(enumerate(nums)), 0, len(nums) - 1)
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums_sorted[left][1] + nums_sorted[right][1] < target:
                left += 1
            elif nums_sorted[left][1] + nums_sorted[right][1] > target:
                right -= 1
            elif left != right:
                if nums_sorted[left][0] < nums_sorted[right][0]:
                    return [nums_sorted[left][0], nums_sorted[right][0]]
                else:
                    return [nums_sorted[right][0], nums_sorted[left][0]]

if __name__ == '__main__':
    nums = [-1, -2, -3, -4, -5]
    target = -8
    Test = Solution()
    print(Test.twoSum(nums, target))