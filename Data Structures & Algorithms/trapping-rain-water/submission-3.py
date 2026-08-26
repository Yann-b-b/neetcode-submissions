class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_left = height[i]
        max_right = height[j]
        tot = 0
        for k in range(0,len(height)):
            # what are the conditions necessary for filling water
            if max_left > max_right:
                tot+= max(0,max_right-height[j])
                j-=1
                max_right = max(max_right, height[j])
            elif max_left <= max_right:
                tot+= max(0,max_left-height[i])
                i+=1
                if i >=len(height):
                    break
                max_left = max(max_left, height[i])
            #conditions for moving in?
        return tot