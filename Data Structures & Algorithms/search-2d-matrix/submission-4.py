class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1
        while left <= right:
            middle = (left + right) // 2
            if matrix[middle][0] <= target and matrix[middle][-1]>=target:
                print(middle)
                break
            elif matrix[middle][0] < target:
                left = middle + 1
            else:
                right = middle - 1
        
      
        row = middle
        print(matrix[row])
        left,right = 0, len(matrix[0])-1
        while left <= right:
            middle = (left + right) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False