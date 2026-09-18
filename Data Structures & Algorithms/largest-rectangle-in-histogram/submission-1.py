class Solution:
    #brute force.
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        the_list_of_heights = sorted(set(heights))
        #print(heights)
        #print(the_list_of_heights)
        max_area = 0

        for i in the_list_of_heights:
            for j in range(0,len(heights)):
                if heights[j] == i:
                    #check left and right until you've got the area of the rectangle           
                    #print("current number")
                    #print(i)
                    length = 0
                    go_left = j
                    go_right= j
                    while go_left>=0 and  i<= heights[go_left]:
                        #print("at this index left")
                        #print(go_left)
                        length+=1
                        go_left-=1
                    while go_right<=len(heights)-1 and  i<=heights[go_right]:
                        #print("at this index right")
                        #print(go_right)
                        length+=1
                        go_right+=1
                    #subtract the repeat of the center number
                    length-=1
                    area = length*i
                    #print("area calculated")
                    #print(area)
                    max_area = max(max_area,area)
        return max_area
    """
    #stacking it up (watched part of the  solution video for this - not the code)
    def largestRectangleArea(self, heights: List[int]) -> int: 
        the_stack = [] 
        max_area = 0
        the_stack.append([0,heights[0]])
        for i in range(1,len(heights)):
            if the_stack[-1][1]<= heights[i]:                      # (1) dropped the broken or-clause
                the_stack.append([i,heights[i]])
            else:
                start = i                                          # (2)
                while the_stack and the_stack[-1][1] > heights[i]: # (3) guard empty
                    get_out = the_stack.pop()
                    area = (i-get_out[0])*get_out[1]
                    max_area = max(area,max_area)
                    start = get_out[0]                             # (2) inherit leftmost index
                the_stack.append([start,heights[i]])               # (2)
        while the_stack:                                           # (4) was `not the_stack`
            get_out = the_stack.pop()
            area = (len(heights)-get_out[0])*get_out[1]            # (4) right edge is the array end
            max_area = max(area,max_area)
        return max_area