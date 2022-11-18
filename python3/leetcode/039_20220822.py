class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        if target < candidates[0]:
            return []
        result = {}
        for i in range(candidates[0], target + 1):
            for j in range(candidates[0], i // 2 + 1):
                if j <= i-j:
                    if i-j in result and j in result:
                        if i not in result:
                            result[i] = []
                        for list1 in result[j]:
                            for list2 in result[i-j]:
                                l = list1 + list2
                                l.sort()
                                if l not in result[i]:
                                    result[i].append(l) 
            if i in candidates:
                if i not in result:
                    result[i] = []
                result[i] += [[i]]
        return result[target] if target in result else []

if __name__ == "__main__":
    Test = Solution()
    print(Test.combinationSum([5], 12))