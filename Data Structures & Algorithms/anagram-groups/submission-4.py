class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if strs == [""]:
            return [[""]]


        out = list()
        sets = dict()
        for string in strs:
            count = [0] * 26
            for ch in string:
                count[ord(ch) - ord('a')] += 1
            
            key = tuple(count)
            if key not in sets:
                sets[key] = len(out)
                out.append([string])
            else:
                out[sets[key]].append(string)
        return out
