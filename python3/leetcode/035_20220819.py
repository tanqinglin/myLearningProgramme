class Solution(object):
    
    def searchInsert(self, nums, target):
        if nums == []:
            return 0
        left, right = 0, len(nums) - 1
        return self.search(nums, left, right, target)

    def search(self, nums, left, right, target):
        
        if left == right:
            if nums[left] < target:
                return left + 1
            else:
                return left
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.search(nums, mid + 1, right, target)
        else:
            return self.search(nums, left, mid, target)   

if __name__ == "__main__":
    Test = Solution()
    print(Test.searchInsert([1,3,5,6], -1))