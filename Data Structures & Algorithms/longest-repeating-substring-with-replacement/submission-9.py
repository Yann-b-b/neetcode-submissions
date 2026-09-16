class Solution:
    #it's max frequency dependent. the window adapts to that.
    def characterReplacement(self, s: str, k: int) -> int:
        #s with upercase english chars and int k
        left,right = 0,0
        mega = 0
        fricking_dict = dict()
        while right< len(s):
            
            fricking_dict[s[right]] = fricking_dict.get(s[right], 0)  +1
            #mega = max(mega,min(right-left, max(fricking_dict.values())+k))
            
            while  (right - left + 1) - max(fricking_dict.values()) > k:
                fricking_dict[s[left]] -= 1
                left+=1
            
            mega = max(mega, right - left + 1) 
            right+=1
        return mega
        

            


            



            

        
        return result

            

