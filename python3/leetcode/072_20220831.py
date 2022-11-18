class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        h, w = len(word1)+1, len(word2)+1
        dp = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            dp[i][0] = i
        for j in range(w):
            dp[0][j] = j
        for i in range(1, h):
            for j in range(1, w):
                dp[i][j] = min(dp[i-1][j-1]+(word1[i-1]!=word2[j-1]), dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]