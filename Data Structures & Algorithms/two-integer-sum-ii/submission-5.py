class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """brute force
        for i in range(0, len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        """
        #binary search
        for i, num in enumerate(numbers):
            tmp = target - num
            left = 0
            right = len(numbers)
            condition = True
            while condition == True:
                mid = int((right-left)/2+left)
                if numbers[mid] > tmp:
                    right = mid
                    left = left
                elif numbers[mid] < tmp:
                    right = right
                    left = mid
                else:
                    return [i + 1, mid +1]
                if mid == int((right-left)/2+left):
                    condition = False

        return []
            