class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s and t return true if they are anagrams
        #dictionary
        a = dict()
        b = dict()
        #initial length check
        if len(s)!=len(t):
            return False
            
        for ch in s:
            a[ch] = a.get(ch, 0) +1
        for ch in t:
            b[ch] = b.get(ch, 0) +1
        
        for key in a:
            if key not in b.keys():
                return False
            if a[key] == b[key]:
                continue
            else:
                return False

        return True