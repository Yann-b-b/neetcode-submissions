class Solution:

     def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window 
        window_size = len(s1)
        if window_size > len(s2):
            return False
        
        #record into a hashmap
        s1_dict = {chr(i): 0 for i in range(97, 123)} 
        window_dict = {chr(i): 0 for i in range(97, 123)}
        
        for i in range(0,window_size):
            s1_dict[s1[i]] = s1_dict.get(s1[i],0)+1
            window_dict[s2[i]] = window_dict.get(s2[i],0)+1
        
        
        c = 0
        for i in range(window_size,len(s2)):
            c+=1
            print(c)
            print(window_dict)
            print(s1_dict)
            if s1_dict == window_dict:
                
                print(s1_dict)
                print(window_dict)
                return True
            window_dict[s2[i]] += 1
            window_dict[s2[i - window_size]] -= 1
        if s1_dict == window_dict:
                
                print(s1_dict)
                print(window_dict)
                return True
    
        
        return False

"""
#naive solution O(n*mlogm)
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
"""            
            