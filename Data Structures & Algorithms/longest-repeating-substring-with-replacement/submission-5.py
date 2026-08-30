class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #left right thing maybe 
        left,right = 0,0
        result = 0
        fricking_dict = dict()
        while right != len(s):

            fricking_dict[s[right]] = fricking_dict.get(s[right], 0) + 1
            max_value = max(fricking_dict.values())
            window_size = right-left +1
            result = max(result, min(max_value+k,window_size))
            #what are the conditions?
            if window_size - max_value > k:
                fricking_dict[s[left]]-=1
                left+=1
            
            right+=1
            
            

        
        return result

            

