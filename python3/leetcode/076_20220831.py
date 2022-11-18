class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
    
        dict = {}
        for c in t:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
        
        i = b = l = -1
        bs = ls = len(s)+1
        location = {}
        
        while i + 1 < len(s):
            
            i += 1
            
            if s[i] in dict:
                if not location:
                    b = i
                dict[s[i]] -= 1
                if dict[s[i]] == 0:
                    del dict[s[i]]
                if s[i] not in location:
                    location[s[i]] = [i]
                else:
                    location[s[i]] += [i]
                if not dict:
                    l = i - b + 1
                    if l < ls:
                        bs, ls = b, l
            
            elif s[i] in location:
                loc = location[s[i]][0]
                if len(location[s[i]]) > 1:
                    location[s[i]] = location[s[i]][1:] + [i]
                else:
                    location[s[i]] = [i]
                keys = list(location.keys())
                for key in keys: # dict changed exception
                    for j in range(len(location[key])-1, -1, -1):
                        if location[key][j] < loc:
                            location[key] = location[key][j+1:]
                            if location[key] == []:
                                del location[key]
                            if key in dict:
                                dict[key] += j+1
                            else:
                                dict[key] = j+1
                            break
                min = len(s)
                for key in location:
                    if location[key][0] < min:
                        min = location[key][0]
                b = min        
                if not dict:
                    l = i - b + 1
                    if l < ls:
                        bs, ls = b, l
        
        if l != -1:
            return s[bs : bs + ls]
        else:
            return ""


if __name__ == "__main__":
    Test = Solution()
    print(Test.minWindow(s = "aaaaaaaaaaaabbbbbcdd", t = "abcdd"))