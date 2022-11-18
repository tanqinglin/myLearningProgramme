class Solution:
    def findSubstring(self, s, words):
        if s == '' or words == []:
            return []
        L, location = [], []
        for word in words:
            exist = 0
            for i in range(len(location)):
                if location[i][0] == word:
                    location[i][1] += 1
                    exist = 1
                    break
            if exist == 0:
                location.append([word, 1, []])

        subLen = len(words[0])
        start, p, k = 0, 0, 0

        while start <= len(s) - subLen * len(words):
            
            while p < len(words) and not k:
                substring = s[start + p * subLen : start + (p + 1) * subLen]
                find = False
                
                for i in range(len(location)):
                    if substring == location[i][0]:
                        find = True
                        if location[i][1] > len(location[i][2]):
                            location[i][2].append(start + p * subLen)
                            p += 1
                            break
                        else:
                            temp = location[i][2][0]
                            k = 1
                            break
                if not find:
                    k = 2

            if p == len(words):
                L.append(start)
                # for i in range(len(location)):
                #     if s[start : start + subLen] == location[i][0]:
                #         del location[i][2][0]
                #         break
                
            # elif k == 1:
            #     num = 0
            #     for i in range(len(location)):
            #         for j in range(len(location[i][2]) - 1, -1, -1):
            #             if location[i][2][j] <= temp:
            #                 if location[i][2][j] == temp:
            #                     no = i
            #                 del location[i][2][:j+1]
            #                 num += j + 1
            #     start += num * subLen
            #     p += 1 - num
            #     k = 0
            #     location[no][2].append(start + (p - 1) * subLen)

            # elif k == 1 or k == 2:
            for i in range(len(location)):
                location[i][2] = []
            start += 1
            p, k = 0, 0
            
            if start + len(words) * subLen > len(s):
                return L

if __name__ == "__main__":
    Test = Solution()
    print(Test.findSubstring("abaababbaba", ["ba","ab","ab"]))