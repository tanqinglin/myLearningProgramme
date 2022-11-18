class Solution(object):
    
    def searchRange(self, nums, target):
        if nums == []:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        left, right = self.searchLeft(nums, left, right, target)
        return [left, right]

    def searchLeft(self, nums, left, right, target):
        
        if left > right:
            return [-1, -1]
        
        mid = (left + right) // 2
        if nums[mid] == target:
            left = right = mid
            while left - 1 >=0 and nums[left - 1] == target:
                left -= 1
            while right + 1 < len(nums) and nums[right + 1] == target:
                right += 1
            return [left, right]
        elif nums[mid] < target:
            return self.searchLeft(nums, mid + 1, right, target)
        else:
            return self.searchLeft(nums, left, mid - 1, target)    

if __name__ == "__main__":
    Test = Solution()
    print(Test.searchRange([5,7,7,8,8,10], 8))