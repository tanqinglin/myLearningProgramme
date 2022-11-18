class Solution(object):
    def maxArea(self, height):
        DP = [[0]*len(height) for i in len(height)]
        maxVolume = DP[0][-1] = min(height[0], height[-1]) * (len(height) - 1)
        for i in range(len(height) - 2, 0, -1):
            if height[maxRight] < height[i]:
                DP[0][i] = min(height[0], height[i]) * i
                if DP[0][i] > maxVolume:
                    maxVolume = DP[0][i]
        for i in range(1, len(height)):
            for j in range(i + 1, len(height)):
                maxInCol = find(max(DP[:,j]))


            
if __name__ == '__main__':
    Test = Solution()
    Test.maxArea([1,8,6,2,5,4,8,3,7])