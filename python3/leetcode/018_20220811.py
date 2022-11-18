# -*- coding:utf-8 -*-

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        L = []
        for i in range(0, len(nums)-3):
            for j in range(i+1, len(nums)-2):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    result = nums[i] + nums[j] + nums[k] + nums[l]
                    if result == target and [nums[i], nums[j], nums[k], nums[l]] not in L:
                        L.append([nums[i], nums[j], nums[k], nums[l]])
                    elif result < target:
                        k += 1
                    else:
                        l -= 1
        return L

if __name__ == '__main__':
    Test = Solution()
    print(Test.fourSum([1,0,-1,0,-2,2], 0))