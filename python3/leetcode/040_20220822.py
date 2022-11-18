class Solution:

    def __init__(self):
        self.L = []

    def combination(self, candidates, target, list):
        if target == 0 and list not in self.L:
            self.L.append(list)
        
        elif candidates == [] or candidates[-1] * len(candidates) < target:
            return
        
        else:
            l = len(candidates) - 1
            while l >= 0 and target < candidates[l]:
                l -= 1
            if l >= 0:
                self.combination(candidates[:l], target - candidates[l], [candidates[l]] + list)
                if l > 0:
                    self.combination(candidates[:l], target, list)
    
    def combinationSum2(self, candidates, target):
        candidates.sort()
        val = candidates[-1]
        count = 0
        for i in range(len(candidates) - 1, -1, -1):
            if val == candidates[i]:
                count += 1
            if val != candidates[i]:
                if count > target // val:
                    candidates = candidates[:i+1+target // val] + candidates[i+1+count:]
                val = candidates[i]
                count = 1
        
        if i == 0 and count > target // val:
            candidates = candidates[:target // val] + candidates[count:]

        self.combination(candidates, target, [])
        return self.L

if __name__ == "__main__":
    Test = Solution()
    print(Test.combinationSum2([1,5,2,3,1,5,1,2,4,1,4], 3))