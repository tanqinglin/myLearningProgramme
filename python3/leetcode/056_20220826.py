class Solution:

    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            else:
                out += i,
        return out

if __name__ == "__main__":
    Test = Solution()
    print(Test.merge([[1,4],[5,6]]))