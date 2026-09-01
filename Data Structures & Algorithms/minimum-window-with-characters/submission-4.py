class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #sliding window
        comp_dict = dict()
        window_dict = dict()

        for i in range(0,len(t)):
            comp_dict[t[i]] = comp_dict.get(t[i],0)+1
        
        comp_count = len(comp_dict)   # number of DISTINCT chars to satisfy
        wind_count = 0
        cur_min_len = None
        out = ""
        left = 0
        #print("comp dict")
        #print(comp_dict)
        #print("Loop")
        for i in range(0,len(s)):

            
            window_dict[s[i]] = window_dict.get(s[i],0)+1
            if s[i] in comp_dict.keys() and window_dict[s[i]] == comp_dict[s[i]]:
                wind_count +=1
            #print("new it")
            #print(s[i])
            #if s[i] in comp_dict.keys():
                #print("is in keys")
                #print(comp_dict[s[i]])
            #print(window_dict[s[i]])
            #print(wind_count)
            

            while wind_count == comp_count:
                # record BEFORE shrinking — window is valid right now
                if cur_min_len is None or (i - left + 1) < cur_min_len:
                    cur_min_len = i - left + 1
                    out = s[left:i + 1]

                # remove the char AT left, then move left
                window_dict[s[left]] -= 1
                if s[left] in comp_dict and window_dict[s[left]] < comp_dict[s[left]]:
                    wind_count -= 1
                left += 1
            
        return out