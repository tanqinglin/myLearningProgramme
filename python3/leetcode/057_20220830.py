class Solution(object):
    def insert(self, intervals, newInterval):
        
        i = 0
        while i <= len(intervals):

            if i == len(intervals):
                intervals.insert(i, newInterval)

            if (newInterval[0] > intervals[i][0] and newInterval[0] <= intervals[i][1]) or newInterval[0] == intervals[i][0]:
                intervals[i][1] = max(intervals[i][1], newInterval[1])
                while i+1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                    intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                    intervals.remove(intervals[i+1])
                break

            if newInterval[0] < intervals[i][0]:

                if newInterval[1] < intervals[i][0]:
                    intervals.insert(i, newInterval)
                else:
                    intervals[i] = [ min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                    while i+1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                        intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                        intervals.remove(intervals[i+1])
                break

            i += 1

        return intervals

if __name__ == "__main__":
    Test = Solution()
    print(Test.insert([[1,5],[6,8]], [0,9]))