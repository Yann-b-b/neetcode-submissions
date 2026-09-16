class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """brute force
        for i in range(0, len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        """
        #return indices of two nums such that they add to target
        """
        what is binary search? it's developing a way to quickly
        sort through a sorted array left and right
        chunking down on the size as we go.

        """
        left,right = 0,len(numbers)-1
        while numbers[left] + numbers[right]!= target:
            if numbers[left] + numbers[right] >target:
                right-=1
            else:
                left+=1
        
        return [left+1,right+1]   