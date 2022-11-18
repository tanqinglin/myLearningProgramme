class Solution:
    def groupAnagrams(self, strs):
        List, result = [], []
        for s in strs:
            dict = {}
            for char in s:
                if char not in dict:
                    dict[char] = 1
                else:
                    dict[char] += 1
            if dict in List:
                result[List.index(dict)].append(s)
            else:
                List.append(dict)
                result.append([s])
        return result

if __name__ == "__main__":
    Test = Solution()
    print(Test.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))