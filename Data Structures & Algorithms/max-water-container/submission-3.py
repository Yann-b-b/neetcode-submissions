class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #trying to get the max area possible. 
        #we have the heights and the width changes with how far two elemnts are

        #double iterator logic
        #brute force: O(n^2) space is O(1)

        """
        largest = 0
        for i, num in enumerate(heights):
            left = num
            for j in range(i+1, len(heights)):
                right = heights[j]
                container_height = min(left,right)
                container_width =  j-i
                area = container_height *container_width
                if area > largest:
                    largest = area
        return largest

        """
        #what can we do better? 
        # moving the shorter always, while keeping the larger bar helps to find biggest area without trying EVERY optino

        i, j = 0, len(heights)-1
        maximo = 0
        while i!= j:
            area = (j-i)*min(heights[j],heights[i])
            maximo = max(maximo, area)
            if heights[j]<heights[i]:
                j-=1
            else:
                i+=1
        return maximo
