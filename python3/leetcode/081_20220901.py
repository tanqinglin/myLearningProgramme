class Solution:
    def search(self, nums, target: int) -> bool:
        if len(nums) == 0:
            return False
        
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False
        
        if target < nums[0]:
            if nums[-1] < target:
                return False
        
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        if target < nums[0]:

            while left < right and nums[mid] != target:
                if nums[mid] > nums[right] or nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left + right) // 2
        
        else:

            while left < right and nums[mid] != target:
                if nums[mid] < nums[left] or nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                mid = (left + right) // 2
        
        if nums[mid] == target:
            return True
        else:
            return False

if __name__ == "__main__":
    Test = Solution()
    print(Test.search(nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target = 2))