class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window 
        window_size = len(s1)
        if window_size > len(s2):
            return False
        
        #record into a hashmap
        s1_sorted = sorted(s1)
        
        for i in range(0,len(s2)-window_size+1):
            print(s2[i:window_size+i])
            if sorted(s2[i:window_size+i]) == s1_sorted:
                return True
        
        return False
                
            