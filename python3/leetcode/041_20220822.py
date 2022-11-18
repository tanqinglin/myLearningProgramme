class Solution:
    def firstMissingPositive(self, nums):
        if nums == []:
            return 1
        l = len(nums)
        list = [0] * (l + 1)
        for num in nums:
            if num > 0 and num <= l:
                list[num] = 1
        p = 1
        while p <= len(list) - 1 and list[p] == 1:
            p += 1
        return p

if __name__ == "__main__":
    Test = Solution()
    print(Test.firstMissingPositive([0,1,7,8,9,10]))