class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        x = set()
        left, right = 0, 0
        cmax = 0
        c = 0
        for right in range(len(s)):
            if s[right] not in x:
                x.add(s[right])
                c +=1
                #print("here1")
            else:
                #print("here2")
                #print(c)
                cmax = max(cmax,c)
                while s[right] in x:
                    x.remove(s[left])
                    left+=1 
                    c-=1
                x.add(s[right])
                c +=1
                
        cmax = max(cmax,c)
        return cmax
