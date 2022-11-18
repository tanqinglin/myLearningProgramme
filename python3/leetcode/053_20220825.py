class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        i = 0
        m = sum = -10000
        while i < len(nums):

            if sum <= 0:
                m = max(m, sum, nums[i])
                sum = nums[i]
            else:
                if nums[i] < 0:
                    if sum + nums[i] > 0:
                        sum += nums[i]
                    else:
                        sum = 0
                else:
                    sum += nums[i]
                    m = max(m, sum)
            i += 1
        return max(m, sum)

            # logic:
            # ----------------------------------
            # if sum <= 0:
            #     if nums[i] < 0:
            #         if sum <= nums[i]:
            #             m = max(m, nums[i])
            #         else:
            #             m = max(m, sum)
            #     else:
            #         m = max(m, nums[i])
            #     sum = nums[i]
            
            # else:
            #     if nums[i] < 0:
            #         if sum + nums[i] > 0:
            #             sum += nums[i]
            #         else:
            #             sum = 0
            #     else:
            #         sum += nums[i]
            #         m = max(m, sum)

if __name__ == "__main__":
    Test = Solution()
    print(Test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))