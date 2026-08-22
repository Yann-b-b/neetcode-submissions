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
            left, right = i+1, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] > tmp:
                    right = mid - 1
                elif numbers[mid] < tmp:
                    left = mid + 1
                else:
                    return [i + 1, mid + 1]

        return []
            